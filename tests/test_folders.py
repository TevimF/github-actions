import sys

import pytest

from folders import juntar, listar_arquivos, subir


@pytest.fixture
def pasta(tmp_path):
    (tmp_path / "b.txt").write_text("b")
    (tmp_path / "a.txt").write_text("a")
    (tmp_path / "foto.png").write_text("png")
    (tmp_path / "subpasta").mkdir()
    return tmp_path


def test_listar_arquivos_ignora_pastas_e_ordena(pasta):
    assert listar_arquivos(pasta) == ["a.txt", "b.txt", "foto.png"]


def test_listar_arquivos_filtra_extensao(pasta):
    assert listar_arquivos(pasta, ".txt") == ["a.txt", "b.txt"]


def test_listar_arquivos_pasta_vazia(tmp_path):
    assert listar_arquivos(tmp_path) == []


def test_listar_arquivos_pasta_inexistente(tmp_path):
    with pytest.raises(FileNotFoundError):
        listar_arquivos(tmp_path / "nao_existe")


def test_subir_um_nivel(pasta):
    assert subir(pasta / "subpasta") == pasta


def test_subir_varios_niveis(tmp_path):
    fundo = tmp_path / "x" / "y" / "z"
    fundo.mkdir(parents=True)
    assert subir(fundo, 3) == tmp_path


def test_subir_para_na_raiz(tmp_path):
    # / no Mac/Linux e C:\ no Windows
    assert subir(tmp_path, 100) == subir(tmp_path, 101)
    assert str(subir(tmp_path, 100)) == tmp_path.anchor


@pytest.mark.skipif(sys.platform != "win32", reason="Windows")
def test_juntar_windows():
    assert juntar("a", "b", "c.txt") == "a\\b\\c.txt"


@pytest.mark.skipif(sys.platform == "win32", reason="Mac/Linux")
def test_juntar_unix():
    assert juntar("a", "b", "c.txt") == "a/b/c.txt"
