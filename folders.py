from pathlib import Path


def listar_arquivos(pasta, extensao=None):
    pasta = Path(pasta)
    return sorted(p.name for p in pasta.iterdir()
                  if p.is_file() and (extensao is None or p.suffix == extensao))


def subir(caminho, niveis=1):
    caminho = Path(caminho)
    for _ in range(niveis):
        caminho = caminho.parent
    return caminho


def juntar(*partes):
    return str(Path(*partes))