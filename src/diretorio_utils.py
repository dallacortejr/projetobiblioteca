"""Funções utilitárias para gerenciamento de diretórios."""

from __future__ import annotations

import shutil
from pathlib import Path


def diretorio_existe(caminho: Path) -> bool:
    """Verifica se um diretório existe."""
    return caminho.exists() and caminho.is_dir()


def criar_diretorio(caminho: Path) -> Path:
    """Cria um diretório, incluindo diretórios intermediários."""
    caminho.mkdir(parents=True, exist_ok=True)
    return caminho


def listar_diretorios(caminho_base: Path) -> list[Path]:
    """Lista diretórios imediatamente abaixo de um caminho base."""
    criar_diretorio(caminho_base)
    return sorted([item for item in caminho_base.iterdir() if item.is_dir()])


def remover_diretorio(caminho: Path, forcar: bool = False) -> bool:
    """
    Remove um diretório.

    Se forcar=True, remove diretórios com conteúdo.
    Se forcar=False, remove apenas diretórios vazios.
    """
    if not diretorio_existe(caminho):
        return False

    if forcar:
        shutil.rmtree(caminho)
    else:
        caminho.rmdir()

    return True
