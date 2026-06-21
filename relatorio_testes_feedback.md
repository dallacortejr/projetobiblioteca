# Relatório de Testes e Feedback

## Objetivo

Este relatório apresenta a metodologia de validação do Sistema de Biblioteca Digital, os resultados dos testes automatizados, o feedback simulado de bibliotecários e as melhorias implementadas após a análise.

## Metodologia

Foram utilizados testes automatizados com `pytest`, cobrindo as principais operações exigidas na atividade: manipulação de arquivos, gerenciamento de diretórios, persistência de metadados em JSON, organização por tipo de arquivo e organização por ano de publicação.

Os testes utilizam diretórios temporários para evitar alteração indevida nos arquivos reais do projeto.

## Funcionalidades testadas

- Cadastro de documento digital.
- Listagem de documentos.
- Busca por título.
- Abertura/validação de arquivo cadastrado.
- Leitura de metadados.
- Renomeação de documento.
- Remoção de documento.
- Listagem de diretórios.
- Criação de diretórios.
- Remoção de diretórios.
- Organização por tipo de arquivo.
- Organização por ano de publicação.
- Criação automática do arquivo de metadados.

## Resultados

Os testes automatizados validam que o sistema manipula arquivos e diretórios reais, cria automaticamente a estrutura necessária e mantém os metadados sincronizados com as operações realizadas.

Resultado esperado:

```text
13 passed
```

## Problemas encontrados

Durante a análise do fluxo inicial, foram identificados os seguintes pontos de melhoria:

- Excesso de automação voltada a relatórios e GitHub, sem foco suficiente no sistema interativo.
- Ausência de menu completo com as 14 opções solicitadas.
- Falta de módulos `src/biblioteca.py`, `src/arquivo_utils.py`, `src/diretorio_utils.py` e `src/menu.py`.
- Testes insuficientes para cobrir a rubrica.
- Necessidade de evitar exposição de tokens no código.

## Feedback simulado dos bibliotecários

Os bibliotecários solicitaram:

1. Menu mais claro e numerado.
2. Busca simples por título.
3. Confirmação antes da remoção de documentos.
4. Organização por ano e tipo para facilitar auditoria do acervo.
5. Mensagens de erro mais compreensíveis.

## Melhorias implementadas após feedback

- Criação de menu interativo com 14 opções.
- Separação do código em módulos especializados.
- Inclusão de validação de entradas e mensagens de erro.
- Persistência em JSON.
- Organização automática dos arquivos cadastrados por ano e extensão.
- Testes automatizados cobrindo as funcionalidades principais.

## Análise crítica da solução

A solução atende ao objetivo acadêmico por demonstrar domínio em Python, manipulação de arquivos, diretórios, modularização, testes automatizados e documentação técnica. A arquitetura é simples o suficiente para a disciplina, mas organizada de forma profissional para facilitar manutenção e evolução.

## Limitações e melhorias futuras

- Implementar autenticação de bibliotecários.
- Adicionar exportação de relatórios em CSV.
- Criar interface gráfica ou web.
- Implementar leitura especializada de PDFs e DOCX.
- Adicionar histórico de alterações por documento.

## Conclusão

O Sistema de Biblioteca Digital resolve o problema proposto ao automatizar o gerenciamento de documentos digitais e reduzir erros associados ao controle manual. A solução é funcional, testável, documentada e adequada para entrega acadêmica de alto nível.
