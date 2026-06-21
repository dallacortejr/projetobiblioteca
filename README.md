# Biblioteca Digital

## Descrição

Sistema acadêmico desenvolvido em Python para gerenciamento de documentos digitais de uma biblioteca universitária.

A solução permite cadastrar, listar, buscar, abrir, consultar, renomear, remover e organizar documentos digitais por tipo de arquivo e ano de publicação. O sistema manipula arquivos e diretórios reais, grava metadados em JSON e oferece uma interface de linha de comando com menu numérico.

## Contextualização do problema

A biblioteca universitária possui documentos digitais como artigos, teses, livros, arquivos PDF, ePUB, DOCX e TXT. A gestão manual desses arquivos é ineficiente e propensa a falhas de rastreabilidade. O sistema proposto automatiza a organização do acervo, melhora o controle dos metadados e simplifica a operação para bibliotecários.

## Objetivo

Criar um sistema funcional, modular e testável em Python para gerenciar documentos digitais, demonstrando domínio em manipulação de arquivos, diretórios, JSON, testes automatizados, Git e GitHub.

## Funcionalidades

- Cadastrar/adicionar documento digital.
- Listar documentos cadastrados.
- Buscar documento por título.
- Abrir documento cadastrado.
- Exibir informações detalhadas e metadados.
- Criar arquivo de metadados automaticamente.
- Renomear documentos.
- Remover documentos.
- Listar diretórios do sistema.
- Criar diretórios.
- Remover diretórios.
- Organizar documentos por tipo de arquivo.
- Organizar documentos por ano de publicação.
- Encerrar o sistema pelo menu.

## Estrutura do projeto

```text
biblioteca_digital/
├── main.py
├── requirements.txt
├── README.md
├── CONTRIBUTING.md
├── relatorio_testes_feedback.md
├── .gitignore
├── data/
│   └── documentos.json
├── documentos/
│   ├── .gitkeep
│   ├── boas_praticas_pesquisa_academica.txt
│   └── introducao_ciencia_de_dados.txt
├── src/
│   ├── __init__.py
│   ├── arquivo_utils.py
│   ├── biblioteca.py
│   ├── diretorio_utils.py
│   └── menu.py
└── tests/
    ├── __init__.py
    └── test_biblioteca.py
```

## Tecnologias utilizadas

- Python 3.
- pathlib.
- os.
- shutil.
- json.
- pytest.
- Git e GitHub.

## Instalação

Clone o repositório:

```bash
git clone https://github.com/dallacortejr/projetobiblioteca.git
cd projetobiblioteca
```

Crie e ative um ambiente virtual:

```bash
python -m venv .venv
```

No Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

No Linux/macOS:

```bash
source .venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

## Como executar

```bash
python main.py
```

O sistema abrirá um menu interativo com 14 opções.

## Como rodar os testes

```bash
pytest -q
```

Resultado esperado:

```text
13 passed
```

## Exemplo de uso no terminal

```text
1. Cadastrar/adicionar documento digital
2. Listar todos os documentos cadastrados
3. Buscar documento por título
...
14. Sair
```

Para cadastrar um documento, informe o caminho de um arquivo existente no computador ou no ambiente Colab.

## GitHub e colaboração

Fluxo sugerido:

```bash
git checkout -b feature/cadastro-documentos
git add .
git commit -m "feat: implementa cadastro de documentos digitais"
git push -u origin feature/cadastro-documentos
```

Depois, abra uma Pull Request no GitHub para revisão antes de mesclar na branch principal.

## Explicação resumida da solução

O projeto foi dividido em módulos para separar responsabilidades: `arquivo_utils.py` manipula arquivos e JSON; `diretorio_utils.py` manipula diretórios; `biblioteca.py` concentra as regras de negócio; `menu.py` fornece a interface de linha de comando; e `tests/test_biblioteca.py` valida as principais funcionalidades. Essa estrutura facilita manutenção, testes, colaboração e avaliação acadêmica.
