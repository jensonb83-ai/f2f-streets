"""Reproduce the 2.15 image update from the unchanged 2.14 source files."""
from pathlib import Path
import base64, io, json, re
import fitz
from PIL import Image, ImageChops, ImageFilter, ImageOps

root = Path(__file__).resolve().parents[1]
html = root / 'index.html'
s = html.read_text(encoding='utf-8')
assert '<small>2.14</small>' in s, 'Expected original version 2.14; no changes applied.'
items = json.loads(re.search(r'const SHOP_ITEMS=(\[.*?\]);', s, re.S)[1])
assert len(items) == 19
D = root / 'downloads'
W,H = 1600,960

def crop_white(im):
    mask = ImageChops.difference(im, Image.new('RGB', im.size, 'white')).convert('L').point(lambda p: 255 if p > 27 else 0)
    b = mask.getbbox()
    if not b: return im
    x,y,r,t = b; pad = max(8,int(min(im.size)*.025))
    return im.crop((max(0,x-pad),max(0,y-pad),min(im.width,r+pad),min(im.height,t+pad)))

def pdf_image(path, first_cards=False):
    with fitz.open(path) as d:
        p = d[0]; clip=p.rect
        if first_cards: clip = fitz.Rect(0,0,p.rect.width,p.rect.height*.35)
        scale= min(4, 1800/max(clip.width,clip.height))
        pix=p.get_pixmap(matrix=fitz.Matrix(scale,scale),clip=clip,alpha=False)
        return crop_white(Image.frombytes('RGB',(pix.width,pix.height),pix.samples))

def fit(im,size):
    return ImageOps.contain(im,size,Image.Resampling.LANCZOS)

def frame(im):
    c=Image.new('RGB',(W,H),'#f5edf2'); a=fit(im,(W-72,H-64)); c.paste(a,((W-a.width)//2,(H-a.height)//2)); return c

for item in items:
    path=root/item['image']; src=root/item['href']; k=item['id']
    if src.suffix.lower()=='.pdf':
        out=frame(pdf_image(src,k in {'karten345','ngo16','joker6','impro12'}))
    elif k=='printpaket':
        out=Image.new('RGB',(W,H),'#f5edf2')
        for f,box in [('345_Spielkarten.pdf',(30,30,760,900)),('Postkarte_A6_Aktuell.pdf',(790,30,780,900))]:
            x,y,w,h=box; a=fit(pdf_image(D/f),(w,h));out.paste(a,(x+(w-a.width)//2,y+(h-a.height)//2))
    else:
        # Existing ZIP/CSV previews are the available source; preserve their contents.
        with Image.open(path) as old: out=frame(old.convert('RGB').crop((145,174,1125,660)))
    out.save(path,'WEBP',quality=93,method=6)

count=0
assets=root / "assets" / "portraits"
assets.mkdir(parents=True,exist_ok=True)

def enhance(m):
    global count
    with Image.open(io.BytesIO(base64.b64decode(m[3]))) as original:
        im=original.convert('RGB'); scale=max(1,min(3,440/im.width))
        im=im.resize((round(im.width*scale),round(im.height*scale)),Image.Resampling.LANCZOS)
        im=im.filter(ImageFilter.UnsharpMask(radius=1.25,percent=115,threshold=3))
        im.save(assets / (m[1]+'.webp'),'WEBP',quality=90,method=5)
    count+=1
    return '"'+m[1]+'":"assets/portraits/'+m[1]+'.webp"'

s=re.sub(r'"((?:N|P)\d{3}|J[CT]\d)":"data:image/(jpeg|png);base64,([A-Za-z0-9+/=]+)"',enhance,s)
assert count==134, count
css='''\n/* 2.15: keep original framing; no hover-induced blur or crop. */
.cardPic{height:clamp(150px,22vw,220px);overflow:hidden}
.cardPic img,.galleryCard .cardPic img{object-fit:contain;object-position:center;display:block}
.galleryCard .cardPic{height:230px}
.shopMedia{height:auto;aspect-ratio:5/3;background:#f5edf2}
.shopMedia img{object-fit:contain;object-position:center;transition:none}
.shopProduct:hover .shopMedia img{transform:none}
@media(max-width:480px){.cardPic{height:175px}.galleryCard .cardPic{height:210px}.shopMedia{height:auto;aspect-ratio:5/3}}
'''
s=s.replace('</style></head>',css+'</style></head>',1).replace('2.14','2.15')
html.write_text(s,encoding='utf-8')
readme=root/'README.md';readme.write_text(readme.read_text(encoding='utf-8').replace('Version **2.14**','Version **2.15**'),encoding='utf-8')
(root/'AENDERUNGEN_2.15.txt').write_text('2.15 – 19 Shop-Vorschauen in 1600 × 960, PDF-Vorschauen neu gerendert; 134 Charakterporträts als separate WebP-Dateien vorsichtig hochskaliert und nachgeschärft; QR-Code unverändert, ohne neue Bilddetails zu erfinden. Bildausschnitte vollständig sichtbar, Hover-Zoom entfernt. Spielregeln, 19 Downloads und Datenschutzlogik unverändert.\n',encoding='utf-8')
print('2.15:',count,'portraits and',len(items),'shop previews')
