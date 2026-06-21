"""Testes automatizados para a biblioteca digital."""

from pathlib import Path

import pytest

from src.biblioteca import BibliotecaDigital
from src.diretorio_utils import criar_diretorio, listar_diretorios, remover_diretorio


@pytest.fixture
def biblioteca(tmp_path):
    """Cria uma biblioteca temporária para os testes."""
    return BibliotecaDigital(base_dir=tmp_path)


@pytest.fixture
def arquivo_origem(tmp_path):
    """Cria um arquivo temporário usado como origem de cadastro."""
    arquivo = tmp_path / "origem_documento.txt"
    arquivo.write_text("Conteúdo acadêmico de teste.", encoding="utf-8")
    return arquivo


def test_cadastro_de_documento(biblioteca, arquivo_origem):
    documento = biblioteca.cadastrar_documento(
        origem=arquivo_origem,
        titulo="Teste de Cadastro",
        autores="Autor Teste",
        ano_publicacao=2024,
        tipo_documento="Artigo",
    )

    assert documento["titulo"] == "Teste de Cadastro"
    assert Path(biblioteca.base_dir / documento["caminho"]).exists()


def test_listagem_de_documentos(biblioteca, arquivo_origem):
    biblioteca.cadastrar_documento(
        arquivo_origem,
        "Listagem",
        "Autor",
        2024,
        "Livro",
    )

    documentos = biblioteca.listar_documentos()

    assert len(documentos) == 1
    assert documentos[0]["titulo"] == "Listagem"


def test_busca_por_titulo(biblioteca, arquivo_origem):
    biblioteca.cadastrar_documento(
        arquivo_origem,
        "Pesquisa em Dados",
        "Autor",
        2023,
        "Tese",
    )

    resultados = biblioteca.buscar_documento_por_titulo("dados")

    assert len(resultados) == 1
    assert resultados[0]["titulo"] == "Pesquisa em Dados"


def test_abertura_de_documento(biblioteca, arquivo_origem):
    documento = biblioteca.cadastrar_documento(
        arquivo_origem,
        "Abrir Arquivo",
        "Autor",
        2022,
        "Artigo",
    )

    caminho = biblioteca.abrir_documento(documento["id"])

    assert caminho.exists()


def test_leitura_de_metadados(biblioteca, arquivo_origem):
    documento = biblioteca.cadastrar_documento(
        arquivo_origem,
        "Ler Metadados",
        "Autor",
        2021,
        "Livro",
    )

    informacoes = biblioteca.ler_informacoes_documento(documento["id"])

    assert informacoes["metadados"]["titulo"] == "Ler Metadados"
    assert informacoes["arquivo_existe"] is True
    assert "Conteúdo acadêmico" in informacoes["previa_textual"]


def test_renomeacao_de_documento(biblioteca, arquivo_origem):
    documento = biblioteca.cadastrar_documento(
        arquivo_origem,
        "Nome Antigo",
        "Autor",
        2020,
        "Artigo",
    )

    atualizado = biblioteca.renomear_documento(
        documento["id"],
        "nome_novo",
        "Nome Novo",
    )

    assert atualizado["titulo"] == "Nome Novo"
    assert atualizado["arquivo"] == "nome_novo.txt"
    assert (biblioteca.base_dir / atualizado["caminho"]).exists()


def test_remocao_de_documento(biblioteca, arquivo_origem):
    documento = biblioteca.cadastrar_documento(
        arquivo_origem,
        "Remover",
        "Autor",
        2024,
        "Artigo",
    )

    removido = biblioteca.remover_documento(documento["id"])

    assert removido is True
    assert biblioteca.listar_documentos() == []


def test_listagem_de_diretorios(tmp_path):
    criar_diretorio(tmp_path / "docs")
    diretorios = listar_diretorios(tmp_path)

    assert any(diretorio.name == "docs" for diretorio in diretorios)


def test_criacao_de_diretorio(tmp_path):
    caminho = criar_diretorio(tmp_path / "novo_diretorio")

    assert caminho.exists()
    assert caminho.is_dir()


def test_remocao_de_diretorio(tmp_path):
    caminho = criar_diretorio(tmp_path / "diretorio_removivel")
    removido = remover_diretorio(caminho)

    assert removido is True
    assert not caminho.exists()


def test_organizacao_por_tipo(biblioteca, arquivo_origem):
    biblioteca.cadastrar_documento(
        arquivo_origem,
        "Documento TXT",
        "Autor",
        2024,
        "Artigo",
    )

    agrupado = biblioteca.listar_por_tipo()

    assert ".txt" in agrupado
    assert len(agrupado[".txt"]) == 1


def test_organizacao_por_ano(biblioteca, arquivo_origem):
    biblioteca.cadastrar_documento(
        arquivo_origem,
        "Documento 2024",
        "Autor",
        2024,
        "Artigo",
    )

    agrupado = biblioteca.listar_por_ano()

    assert 2024 in agrupado
    assert len(agrupado[2024]) == 1


def test_criar_arquivo_metadados(biblioteca):
    caminho = biblioteca.criar_arquivo_metadados()

    assert caminho.exists()
    assert caminho.name == "documentos.json"
