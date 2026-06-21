# Guia de Contribuição

## Objetivo

Este guia orienta como contribuir com o projeto Biblioteca Digital usando Git e GitHub de forma organizada.

## Fluxo recomendado

1. Atualize a branch principal:

```bash
git checkout main
git pull origin main
```

2. Crie uma branch para sua alteração:

```bash
git checkout -b feature/nome-da-funcionalidade
```

3. Faça as alterações no código.

4. Execute os testes:

```bash
pytest -q
```

5. Adicione os arquivos alterados:

```bash
git add .
```

6. Crie um commit claro:

```bash
git commit -m "feat: descreve a funcionalidade implementada"
```

7. Envie para o GitHub:

```bash
git push -u origin feature/nome-da-funcionalidade
```

8. Abra uma Pull Request para revisão.

## Padrão de commits

Use mensagens curtas, claras e descritivas:

- `feat: adiciona cadastro de documentos`
- `fix: corrige validação de ano de publicação`
- `docs: atualiza instruções do README`
- `test: adiciona testes para remoção de diretórios`
- `refactor: reorganiza funções utilitárias`

## Boas práticas

- Não envie senhas, tokens ou chaves de API para o repositório.
- Execute os testes antes de abrir Pull Request.
- Mantenha nomes de funções e variáveis em `snake_case`.
- Use comentários somente quando ajudarem a entender decisões relevantes.
- Prefira alterações pequenas e bem descritas.

## Pull Requests

A Pull Request deve conter:

- Resumo da alteração.
- Funcionalidades impactadas.
- Evidência de testes executados.
- Observações sobre limitações ou melhorias futuras.

O arquivo `CONTRIBUTING.md` pode permanecer na raiz do projeto, pois o GitHub reconhece esse formato como documentação de contribuição.
