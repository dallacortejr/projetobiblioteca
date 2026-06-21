"""Lógica principal do Sistema de Biblioteca Digital."""

from __future__ import annotations

import re
import uuid
from datetime import datetime
from pathlib import Path
from typing import Any

from src.arquivo_utils import (
    abrir_arquivo,
    arquivo_existe,
    copiar_arquivo,
    criar_arquivo,
    garantir_arquivo_json,
    ler_arquivo_texto,
    ler_json,
    remover_arquivo,
    renomear_arquivo,
    escrever_json,
)
from src.diretorio_utils import criar_diretorio, listar_diretorios, remover_diretorio

EXTENSOES_SUPORTADAS = {".pdf", ".epub", ".txt", ".docx", ".mobi", ".azw"}


class BibliotecaDigital:
    """Representa a biblioteca digital e suas operações principais."""

    def __init__(self, base_dir: Path | str | None = None) -> None:
        self.base_dir = Path(base_dir) if base_dir else Path.cwd()
        self.data_dir = self.base_dir / "data"
        self.documentos_dir = self.base_dir / "documentos"
        self.metadata_path = self.data_dir / "documentos.json"
        self.inicializar_estrutura()

    def inicializar_estrutura(self) -> None:
        """Cria as pastas e o JSON de metadados, se ainda não existirem."""
        criar_diretorio(self.data_dir)
        criar_diretorio(self.documentos_dir)
        garantir_arquivo_json(self.metadata_path, [])

    def carregar_documentos(self) -> list[dict[str, Any]]:
        """Carrega os documentos cadastrados no JSON."""
        dados = ler_json(self.metadata_path, [])
        return dados if isinstance(dados, list) else []

    def salvar_documentos(self, documentos: list[dict[str, Any]]) -> None:
        """Salva a lista de documentos no JSON."""
        escrever_json(self.metadata_path, documentos)

    def criar_arquivo_metadados(self) -> Path:
        """Cria explicitamente o arquivo de metadados, caso necessário."""
        garantir_arquivo_json(self.metadata_path, [])
        return self.metadata_path

    def cadastrar_documento(
        self,
        origem: Path | str,
        titulo: str,
        autores: str,
        ano_publicacao: int,
        tipo_documento: str,
    ) -> dict[str, Any]:
        """Cadastra um documento, copia o arquivo e grava os metadados."""
        origem_path = Path(origem)

        if not arquivo_existe(origem_path):
            raise FileNotFoundError(f"Documento de origem não encontrado: {origem_path}")

        extensao = origem_path.suffix.lower()
        if extensao not in EXTENSOES_SUPORTADAS:
            raise ValueError(f"Extensão não suportada: {extensao}")

        ano = self._validar_ano(ano_publicacao)
        titulo_limpo = self._normalizar_nome(titulo)
        identificador = str(uuid.uuid4())[:8]
        nome_arquivo = f"{titulo_limpo}_{identificador}{extensao}"
        destino = self.documentos_dir / str(ano) / extensao.replace(".", "") / nome_arquivo

        copiar_arquivo(origem_path, destino)

        documento = {
            "id": identificador,
            "titulo": titulo.strip(),
            "autores": autores.strip(),
            "ano_publicacao": ano,
            "tipo_documento": tipo_documento.strip(),
            "extensao": extensao,
            "arquivo": nome_arquivo,
            "caminho": str(destino.relative_to(self.base_dir)),
            "data_cadastro": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }

        documentos = self.carregar_documentos()
        documentos.append(documento)
        self.salvar_documentos(documentos)
        return documento

    def listar_documentos(self) -> list[dict[str, Any]]:
        """Retorna todos os documentos cadastrados."""
        return self.carregar_documentos()

    def buscar_documento_por_titulo(self, termo: str) -> list[dict[str, Any]]:
        """Busca documentos pelo título, sem diferenciar maiúsculas/minúsculas."""
        termo_normalizado = termo.strip().lower()
        return [
            documento
            for documento in self.carregar_documentos()
            if termo_normalizado in documento["titulo"].lower()
        ]

    def obter_documento_por_id(self, documento_id: str) -> dict[str, Any] | None:
        """Localiza um documento pelo ID."""
        for documento in self.carregar_documentos():
            if documento["id"] == documento_id:
                return documento
        return None

    def abrir_documento(self, documento_id: str) -> Path:
        """Abre um documento cadastrado ou retorna o caminho em ambiente sem GUI."""
        documento = self._exigir_documento(documento_id)
        return abrir_arquivo(self.base_dir / documento["caminho"])

    def ler_informacoes_documento(self, documento_id: str) -> dict[str, Any]:
        """Retorna metadados e prévia textual do documento."""
        documento = self._exigir_documento(documento_id)
        caminho = self.base_dir / documento["caminho"]

        previa = ""
        if documento["extensao"] == ".txt":
            previa = ler_arquivo_texto(caminho, limite=1000)

        return {
            "metadados": documento,
            "arquivo_existe": arquivo_existe(caminho),
            "caminho_absoluto": str(caminho),
            "previa_textual": previa,
        }

    def renomear_documento(
        self,
        documento_id: str,
        novo_nome_arquivo: str,
        novo_titulo: str | None = None,
    ) -> dict[str, Any]:
        """Renomeia o arquivo físico e atualiza os metadados."""
        documentos = self.carregar_documentos()

        for documento in documentos:
            if documento["id"] == documento_id:
                caminho_atual = self.base_dir / documento["caminho"]
                extensao = documento["extensao"]
                nome_limpo = self._normalizar_nome(Path(novo_nome_arquivo).stem)
                novo_nome = f"{nome_limpo}{extensao}"
                novo_caminho = caminho_atual.with_name(novo_nome)

                renomear_arquivo(caminho_atual, novo_caminho)

                documento["arquivo"] = novo_nome
                documento["caminho"] = str(novo_caminho.relative_to(self.base_dir))
                documento["titulo"] = novo_titulo.strip() if novo_titulo else documento["titulo"]
                documento["data_atualizacao"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                self.salvar_documentos(documentos)
                return documento

        raise ValueError("Documento não encontrado para renomeação.")

    def remover_documento(self, documento_id: str) -> bool:
        """Remove o arquivo físico e exclui o registro de metadados."""
        documentos = self.carregar_documentos()
        novos_documentos = []
        removido = False

        for documento in documentos:
            if documento["id"] == documento_id:
                remover_arquivo(self.base_dir / documento["caminho"])
                removido = True
            else:
                novos_documentos.append(documento)

        if removido:
            self.salvar_documentos(novos_documentos)

        return removido

    def listar_por_tipo(self) -> dict[str, list[dict[str, Any]]]:
        """Agrupa documentos por extensão/tipo de arquivo."""
        agrupado: dict[str, list[dict[str, Any]]] = {}

        for documento in self.carregar_documentos():
            agrupado.setdefault(documento["extensao"], []).append(documento)

        return dict(sorted(agrupado.items()))

    def listar_por_ano(self) -> dict[int, list[dict[str, Any]]]:
        """Agrupa documentos por ano de publicação."""
        agrupado: dict[int, list[dict[str, Any]]] = {}

        for documento in self.carregar_documentos():
            agrupado.setdefault(int(documento["ano_publicacao"]), []).append(documento)

        return dict(sorted(agrupado.items()))

    def listar_diretorios_sistema(self) -> list[Path]:
        """Lista diretórios principais do sistema."""
        return listar_diretorios(self.base_dir)

    def criar_diretorio_sistema(self, nome: str) -> Path:
        """Cria um diretório dentro da pasta do projeto."""
        nome_seguro = self._normalizar_nome(nome)
        return criar_diretorio(self.base_dir / nome_seguro)

    def remover_diretorio_sistema(self, nome: str, forcar: bool = False) -> bool:
        """Remove um diretório dentro da pasta do projeto."""
        nome_seguro = self._normalizar_nome(nome)
        caminho = self.base_dir / nome_seguro

        if caminho in {self.data_dir, self.documentos_dir}:
            raise ValueError("Diretórios essenciais do sistema não podem ser removidos.")

        return remover_diretorio(caminho, forcar=forcar)

    def criar_documento_exemplo(self, nome: str, conteudo: str) -> Path:
        """Cria arquivo de exemplo para demonstração e testes manuais."""
        return criar_arquivo(self.documentos_dir / nome, conteudo)

    def _exigir_documento(self, documento_id: str) -> dict[str, Any]:
        documento = self.obter_documento_por_id(documento_id)
        if documento is None:
            raise ValueError("Documento não encontrado.")
        return documento

    @staticmethod
    def _validar_ano(ano: int) -> int:
        ano_int = int(ano)
        ano_atual = datetime.now().year

        if ano_int < 1500 or ano_int > ano_atual + 1:
            raise ValueError("Ano de publicação inválido.")

        return ano_int

    @staticmethod
    def _normalizar_nome(nome: str) -> str:
        nome = nome.strip().lower()
        nome = re.sub(r"[^a-z0-9áàâãéèêíïóôõöúçñ]+", "_", nome)
        nome = re.sub(r"_+", "_", nome).strip("_")
        return nome or "documento"
