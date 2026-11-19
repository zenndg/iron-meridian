"""Gera a arte do Iron Meridian a partir das imagens em tmp/arte.

Uso: python3 scripts/gera-arte-telas.py tmp/arte .

As imagens de origem (1-fundo.png a 5-metal.png) ficam em tmp/arte/, fora do git;
os prompts que as geraram estão em tmp/arte/*.md.

Saída:
- resourcepacks/Iron Meridian UI/ (pack.mcmeta, pack.png, botões, sliders, título)
- config/fancymenu/assets/ (fundos e emblema)
- release/instance/iron_meridian.png (ícone da instância no Prism)
"""
import json
import sys
from pathlib import Path

from PIL import Image, ImageEnhance, ImageFilter

ARTE = Path(sys.argv[1])
ROOT = Path(sys.argv[2])
RP = ROOT / "resourcepacks" / "Iron Meridian UI"
WIDGET = RP / "assets/minecraft/textures/gui/sprites/widget"
TITLE = RP / "assets/minecraft/textures/gui/title"
FM = ROOT / "config/fancymenu/assets"
for d in (WIDGET, TITLE, FM):
    d.mkdir(parents=True, exist_ok=True)

CIANO = (64, 220, 255, 255)
PRETO = (16, 16, 18, 255)
LUZ = (118, 120, 126, 255)
SOMBRA = (40, 40, 44, 255)


def tira_verde(path, sem_verde=False):
    """Remove o fundo verde. Com sem_verde, a imagem não tem verde próprio (o nome):
    o corte é mais agressivo e todo reflexo verde da borda sai."""
    im = Image.open(path).convert("RGBA")
    px = im.load()
    w, h = im.size
    for y in range(h):
        for x in range(w):
            r, g, b, _ = px[x, y]
            k = g - max(r, b)
            if sem_verde:
                a = 0 if k > 150 else (255 if k <= 40 else int(255 * (150 - k) / 110))
                if k > 0:
                    g = max(r, b)
                px[x, y] = (r, g, b, a)
                continue
            if g > 200 and k > 150:
                a = 0
            elif g > 160 and k > 90:
                a = int(255 * (150 - k) / 60)
            else:
                a = 255
            if 0 < a < 255 or (a == 255 and k > 60 and g > 150):
                g = max(r, b) + min(k, 40)
            px[x, y] = (r, g, b, a)
    return im.crop(im.getbbox())


def metal(w, h, brilho=1.0, oy=0):
    """Recorte da textura de metal reduzida, para virar pixel art."""
    base = Image.open(ARTE / "5-metal.png").convert("RGB").resize((256, 256), Image.LANCZOS)
    base = ImageEnhance.Contrast(base).enhance(1.6)
    base = ImageEnhance.Brightness(base).enhance(brilho)
    return base.crop((0, oy, w, oy + h)).convert("RGBA")


def moldura(im, borda, luz=LUZ, sombra=SOMBRA, larg=1):
    """Contorno de 1 px e bisel: luz em cima e à esquerda, sombra embaixo e à direita."""
    w, h = im.size
    px = im.load()
    for x in range(w):
        px[x, 0] = borda
        px[x, h - 1] = borda
    for y in range(h):
        px[0, y] = borda
        px[w - 1, y] = borda
    for i in range(1, 1 + larg):
        for x in range(i, w - i):
            px[x, i] = luz
            px[x, h - 1 - i] = sombra
        for y in range(i, h - i):
            px[i, y] = luz
            px[w - 1 - i, y] = sombra
    return im


def rebites(im, cor=(170, 172, 178, 255)):
    w, h = im.size
    px = im.load()
    for x in (4, w - 5):
        px[x, h // 2 - 1] = cor
        px[x, h // 2] = (60, 60, 64, 255)
    return im


def salva(im, nome, mcmeta=None):
    im.save(WIDGET / nome)
    if mcmeta:
        (WIDGET / (nome + ".mcmeta")).write_text(json.dumps(mcmeta, indent=2) + "\n")


def nine(w, h, borda):
    return {"gui": {"scaling": {"type": "nine_slice", "width": w, "height": h, "border": borda}}}


# Botões 200x20, borda nine-slice 3 (igual ao Minecraft).
salva(moldura(metal(200, 20, 1.0), PRETO), "button.png", nine(200, 20, 3))
salva(moldura(metal(200, 20, 1.25, 40), CIANO, luz=(150, 230, 255, 255)), "button_highlighted.png", nine(200, 20, 3))
desl = ImageEnhance.Brightness(metal(200, 20, 0.7, 80)).enhance(0.8)
salva(moldura(desl, (10, 10, 12, 255), luz=(58, 58, 62, 255), sombra=(26, 26, 28, 255)), "button_disabled.png", nine(200, 20, 3))

# Trilho do slider 200x20, borda 1: metal afundado (sombra em cima, luz embaixo).
trilho = ImageEnhance.Brightness(metal(200, 20, 0.75, 120)).enhance(0.85)
salva(moldura(trilho, PRETO, luz=SOMBRA, sombra=(70, 70, 76, 255)), "slider.png", nine(200, 20, 1))
salva(moldura(trilho.copy(), CIANO, luz=SOMBRA, sombra=(70, 70, 76, 255)), "slider_highlighted.png", nine(200, 20, 1))

# Alça do slider 8x20, bordas 2/2/2/3.
borda_alca = {"left": 2, "top": 2, "right": 2, "bottom": 3}
salva(moldura(metal(8, 20, 1.4, 160), PRETO, luz=(170, 172, 178, 255)), "slider_handle.png", nine(8, 20, borda_alca))
salva(moldura(metal(8, 20, 1.6, 160), CIANO, luz=(190, 240, 255, 255)), "slider_handle_highlighted.png", nine(8, 20, borda_alca))

# Logo do título: 1024x256, o Minecraft desenha só as 176 linhas de cima (256x44 de 256x64).
nome = tira_verde(ARTE / "4-nome.png", sem_verde=True)
lw = 1000
nh = int(nome.height * lw / nome.width)
logo = Image.new("RGBA", (1024, 256), (0, 0, 0, 0))
logo.alpha_composite(nome.resize((lw, nh), Image.LANCZOS), ((1024 - lw) // 2, (176 - nh) // 2))
logo.save(TITLE / "minecraft.png")
logo.save(TITLE / "minceraft.png")  # a versão rara do logo, com a letra trocada
Image.new("RGBA", (512, 64), (0, 0, 0, 0)).save(TITLE / "edition.png")  # sem "Java Edition"

# Emblema: pack.png, FancyMenu e ícone da instância.
emblema = tira_verde(ARTE / "3-emblema.png")
lado = max(emblema.size)
quad = Image.new("RGBA", (lado, lado), (0, 0, 0, 0))
quad.alpha_composite(emblema, ((lado - emblema.width) // 2, (lado - emblema.height) // 2))
quad.resize((128, 128), Image.LANCZOS).save(RP / "pack.png")
quad.resize((512, 512), Image.LANCZOS).save(FM / "iron_meridian_emblema.png")
quad.resize((256, 256), Image.LANCZOS).save(ROOT / "release/instance/iron_meridian.png")

(RP / "pack.mcmeta").write_text(json.dumps({
    "pack": {"pack_format": 34, "description": "Iron Meridian: botões e logo do pack"}
}, ensure_ascii=False, indent=2) + "\n")

# Fundos em 1920x1080. O da tela inicial ganha uma sombra suave no centro, onde ficam os botões.
fundo = Image.open(ARTE / "1-fundo.png").convert("RGB").resize((1920, 1080), Image.LANCZOS)
mask = Image.new("L", fundo.size, 0)
from PIL import ImageDraw  # noqa: E402
ImageDraw.Draw(mask).rectangle((620, 360, 1300, 900), fill=110)
mask = mask.filter(ImageFilter.GaussianBlur(120))
fundo_ini = Image.composite(Image.new("RGB", fundo.size, (0, 0, 0)), fundo, mask)
fundo_ini.save(FM / "iron_meridian_fundo.jpg", quality=90)
desf = ImageEnhance.Brightness(fundo.filter(ImageFilter.GaussianBlur(14))).enhance(0.55)
desf.save(FM / "iron_meridian_fundo_desfocado.jpg", quality=88)
Image.open(ARTE / "2-carregamento.png").convert("RGB").resize((1920, 1080), Image.LANCZOS).save(
    FM / "iron_meridian_carregamento.jpg", quality=90)
print("ok")
