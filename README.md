# Library Digital Manager

Repositório: [dallacortejr/projetobiblioteca](https://github.com/dallacortejr/projetobiblioteca)

Sistema de gerenciamento de biblioteca digital desenvolvido em Python, pensado para bibliotecas universitárias. Permite organizar documentos digitais (PDF, EPUB, DOCX, MOBI, AZW) por tipo e ano de publicação, além de operações de adição, renomeação e remoção de arquivos.

## Funcionalidades

- Listagem de arquivos por tipo e ano.
- Adição de novos documentos digitais.
- Renomeação de arquivos existentes.
- Remoção de documentos.
- Interface de linha de comando (CLI) via `click`.
- Estrutura de teste automatizado (`pytest`).
- Scripts para gerar arquivos de teste seguros.

## Estrutura do projeto

projetobiblioteca/
│
├── library_manager/ # Core e CLI
│ ├── core.py
│ └── cli.py
│
├── scripts/ # Scripts utilitários
│ └── generate_dummy_docs.py
│
├── tests/ # Testes automatizados
│ └── test_core.py
│
├── docs/ # Documentação
│ ├── usage.md
│ ├── test_report.md
│ └── feedback.md
│
├── README.md
└── CONTRIBUTING.md

bash
Copiar código

## Instalação e execução no Google Colab

1. Clone o repositório:

```bash
!git clone https://github.com/dallacortejr/projetobiblioteca.git
%cd projetobiblioteca
Instale dependências:

bash
Copiar código
!pip install PyPDF2 python-docx ebooklib fpdf click pytest fuzzywuzzy python-dateutil
Gere arquivos de teste:

bash
Copiar código
!python scripts/generate_dummy_docs.py
Teste comandos do CLI:

bash
Copiar código
!python -m library_manager.cli list sample_docs
!python -m library_manager.cli add sample_docs/sample_001.pdf sample_store/
!python -m library_manager.cli rename sample_store/sample_001.pdf novo_nome.pdf
!python -m library_manager.cli remove sample_store/novo_nome.pdf
