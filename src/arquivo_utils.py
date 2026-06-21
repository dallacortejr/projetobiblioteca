"""Funções utilitárias para manipulação de arquivos."""

from __future__ import annotations

import json
import os
import platform
import shutil
import subprocess
from pathlib import Path
from typing import Any


def garantir_arquivo_json(caminho: Path, conteudo_padrao: Any | None = None) -> None:
    """Cria um arquivo JSON com conteúdo padrão, caso ele não exista."""
    caminho.parent.mkdir(parents=True, exist_ok=True)

    if not caminho.exists():
        dados = conteudo_padrao if conteudo_padrao is not None else []
        escrever_json(caminho, dados)


def ler_json(caminho: Path, conteudo_padrao: Any | None = None) -> Any:
    """Lê um arquivo JSON e retorna seu conteúdo."""
    garantir_arquivo_json(caminho, conteudo_padrao)

    try:
        with caminho.open("r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except json.JSONDecodeError:
        return conteudo_padrao if conteudo_padrao is not None else []


def escrever_json(caminho: Path, dados: Any) -> None:
    """Grava dados em um arquivo JSON com indentação legível."""
    caminho.parent.mkdir(parents=True, exist_ok=True)

    with caminho.open("w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=4)


def criar_arquivo(caminho: Path, conteudo: str = "") -> Path:
    """Cria um arquivo físico com conteúdo opcional."""
    caminho.parent.mkdir(parents=True, exist_ok=True)
    caminho.write_text(conteudo, encoding="utf-8")
    return caminho


def copiar_arquivo(origem: Path, destino: Path) -> Path:
    """Copia um arquivo físico para outro local."""
    if not origem.exists() or not origem.is_file():
        raise FileNotFoundError(f"Arquivo de origem não encontrado: {origem}")

    destino.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(origem, destino)
    return destino


def arquivo_existe(caminho: Path) -> bool:
    """Verifica se um arquivo existe."""
    return caminho.exists() and caminho.is_file()


def ler_arquivo_texto(caminho: Path, limite: int = 2000) -> str:
    """Lê o conteúdo textual inicial de um arquivo."""
    if not arquivo_existe(caminho):
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho}")

    with caminho.open("r", encoding="utf-8", errors="replace") as arquivo:
        return arquivo.read(limite)


def renomear_arquivo(caminho_atual: Path, novo_caminho: Path) -> Path:
    """Renomeia ou move um arquivo físico."""
    if not arquivo_existe(caminho_atual):
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho_atual}")

    novo_caminho.parent.mkdir(parents=True, exist_ok=True)
    return caminho_atual.rename(novo_caminho)


def remover_arquivo(caminho: Path) -> bool:
    """Remove um arquivo físico, caso ele exista."""
    if arquivo_existe(caminho):
        caminho.unlink()
        return True
    return False


def abrir_arquivo(caminho: Path) -> Path:
    """
    Solicita abertura do arquivo no sistema operacional.

    Em ambientes sem interface gráfica, como Google Colab, a função valida
    a existência do arquivo e retorna o caminho, sem interromper a execução.
    """
    if not arquivo_existe(caminho):
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho}")

    sistema = platform.system().lower()

    try:
        if sistema == "windows":
            os.startfile(caminho)  # type: ignore[attr-defined]
        elif sistema == "darwin":
            subprocess.Popen(["open", str(caminho)])
        elif sistema == "linux" and os.environ.get("DISPLAY"):
            subprocess.Popen(["xdg-open", str(caminho)])
    except OSError:
        pass

    return caminho
