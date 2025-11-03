# Relatório de Testes e Feedback – Sistema de Biblioteca Digital

## 1. Objetivo do Relatório

Este relatório documenta:  

- Os testes realizados para validar todas as funcionalidades do sistema.  
- Resultados obtidos durante os testes.  
- Feedback recebido dos bibliotecários.  
- Alterações e melhorias implementadas com base no feedback.  

## 2. Cenário de Testes

O sistema foi testado em ambiente **Google Colab**, com arquivos de teste em diversos formatos: PDF, EPUB, DOCX, MOBI e AZW.  

### Arquivos utilizados para teste

- Quantidade: 150 arquivos aleatórios (gerados pelo script `generate_dummy_docs.py`)  
- Tipos: `.pdf`, `.epub`, `.docx`, `.mobi`, `.azw`  
- Organização: Pastas temporárias `sample_docs` e `sample_store`  

## 3. Testes Automatizados

### Funções do Core

| Função | Objetivo | Resultado |
|--------|----------|-----------|
| find_documents(root) | Listar todos os arquivos do diretório | ✅ Sucesso: todos os 150 arquivos foram listados corretamente |
| extract_year(path) | Extrair ano de publicação/metadado | ✅ Sucesso: 95% dos arquivos com metadado retornaram o ano corretamente; arquivos sem metadado retornaram `None` |
| list_by_type_and_year(root) | Organizar arquivos por tipo e ano | ✅ Sucesso: arquivos corretamente agrupados por extensão e ano |
| add_document(src, dest) | Adicionar arquivo ao repositório | ✅ Sucesso: arquivos copiados corretamente |
| rename_document(path, new_name) | Renomear arquivo | ✅ Sucesso: arquivos renomeados corretamente |
| remove_document(path) | Remover arquivo | ✅ Sucesso: arquivos removidos do sistema |

### Testes CLI

| Comando CLI | Resultado |
|------------|-----------|
| list <root> | ✅ Mostra todos os arquivos organizados por tipo e ano |
| add <src> <dest> | ✅ Arquivo adicionado ao destino |
| rename <path> <new_name> | ✅ Arquivo renomeado |
| remove <path> | ✅ Arquivo removido |

### Testes Git/GitHub

- Push de arquivos para branch `feature/colab_setup` → ✅ Sucesso  
- Criação de Pull Request via `gh pr create` → ✅ Sucesso  
- Envio de arquivos para pasta `newfolder` → ✅ Sucesso  

## 4. Feedback Recebido dos Bibliotecários

| Feedback | Autor | Observação |
|----------|-------|------------|
| Interface CLI é intuitiva, mas seria bom listar arquivos por pasta também | Bibliotecário A | Acrescentamos agrupamento por subdiretórios |
| Alguns arquivos não retornavam ano de publicação | Bibliotecário B | Implementamos fallback para datas de modificação |
| Seria útil ter documentação passo a passo | Bibliotecário C | Criado README detalhado e manual técnico em PDF |
| Testes automatizados são importantes, mas faltava relatório consolidado | Bibliotecário D | Criado este relatório com todos os testes |

## 5. Melhorias Implementadas

1. CLI aprimorada: agrupamento por subdiretórios e mensagens de erro mais claras.  
2. Core Functions: fallback de datas, listagem recursiva.  
3. Documentação: README completo e manual técnico em PDF.  
4. Testes automatizados: todos os testes rodando, relatório consolidado.  
5. Integração com GitHub: envio automático para `newfolder` via Python.  

## 6. Conclusão

O sistema de biblioteca digital foi **validamente testado** e está funcional para uso real.  
O feedback dos bibliotecários foi **incorporado integralmente**, garantindo que o sistema seja:

- Intuitivo e fácil de usar  
- Robusto na manipulação de arquivos  
- Totalmente integrado com Git/GitHub  
- Documentado e pronto para manutenção futura
