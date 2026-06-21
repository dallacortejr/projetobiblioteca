"""Interface de linha de comando do Sistema de Biblioteca Digital."""

from __future__ import annotations

from pathlib import Path

from src.biblioteca import BibliotecaDigital


def iniciar_menu() -> None:
    """Inicia o menu interativo do sistema."""
    biblioteca = BibliotecaDigital()

    while True:
        _mostrar_menu()
        opcao = input("Escolha uma opção: ").strip()

        try:
            if opcao == "1":
                _cadastrar_documento(biblioteca)
            elif opcao == "2":
                _listar_documentos(biblioteca)
            elif opcao == "3":
                _buscar_documento(biblioteca)
            elif opcao == "4":
                _abrir_documento(biblioteca)
            elif opcao == "5":
                _ler_informacoes(biblioteca)
            elif opcao == "6":
                caminho = biblioteca.criar_arquivo_metadados()
                print(f"Arquivo de metadados pronto em: {caminho}")
            elif opcao == "7":
                _renomear_documento(biblioteca)
            elif opcao == "8":
                _remover_documento(biblioteca)
            elif opcao == "9":
                _listar_diretorios(biblioteca)
            elif opcao == "10":
                _criar_diretorio(biblioteca)
            elif opcao == "11":
                _remover_diretorio(biblioteca)
            elif opcao == "12":
                _listar_por_tipo(biblioteca)
            elif opcao == "13":
                _listar_por_ano(biblioteca)
            elif opcao == "14":
                print("Sistema encerrado com sucesso.")
                break
            else:
                print("Opção inválida. Digite um número de 1 a 14.")
        except Exception as erro:
            print(f"Erro: {erro}")


def _mostrar_menu() -> None:
    print("\n" + "=" * 60)
    print("SISTEMA DE GERENCIAMENTO DE BIBLIOTECA DIGITAL")
    print("=" * 60)
    print("1. Cadastrar/adicionar documento digital")
    print("2. Listar todos os documentos cadastrados")
    print("3. Buscar documento por título")
    print("4. Abrir documento digital cadastrado")
    print("5. Ler/exibir informações detalhadas do documento")
    print("6. Criar arquivo de metadados")
    print("7. Renomear documento")
    print("8. Remover documento")
    print("9. Listar diretórios do sistema")
    print("10. Criar diretório")
    print("11. Remover diretório")
    print("12. Organizar/listar documentos por tipo de arquivo")
    print("13. Organizar/listar documentos por ano de publicação")
    print("14. Sair")


def _cadastrar_documento(biblioteca: BibliotecaDigital) -> None:
    origem = input("Caminho do arquivo de origem: ").strip()
    titulo = input("Título: ").strip()
    autores = input("Autores: ").strip()
    ano = int(input("Ano de publicação: ").strip())
    tipo = input("Tipo de documento: ").strip()

    documento = biblioteca.cadastrar_documento(
        origem=Path(origem),
        titulo=titulo,
        autores=autores,
        ano_publicacao=ano,
        tipo_documento=tipo,
    )

    print(f"Documento cadastrado com sucesso. ID: {documento['id']}")


def _listar_documentos(biblioteca: BibliotecaDigital) -> None:
    documentos = biblioteca.listar_documentos()

    if not documentos:
        print("Nenhum documento cadastrado.")
        return

    for documento in documentos:
        _imprimir_resumo(documento)


def _buscar_documento(biblioteca: BibliotecaDigital) -> None:
    termo = input("Digite parte do título: ").strip()
    resultados = biblioteca.buscar_documento_por_titulo(termo)

    if not resultados:
        print("Nenhum documento encontrado.")
        return

    for documento in resultados:
        _imprimir_resumo(documento)


def _abrir_documento(biblioteca: BibliotecaDigital) -> None:
    documento_id = input("ID do documento: ").strip()
    caminho = biblioteca.abrir_documento(documento_id)
    print(f"Documento validado para abertura: {caminho}")


def _ler_informacoes(biblioteca: BibliotecaDigital) -> None:
    documento_id = input("ID do documento: ").strip()
    informacoes = biblioteca.ler_informacoes_documento(documento_id)
    metadados = informacoes["metadados"]

    print("\nINFORMAÇÕES DO DOCUMENTO")
    print("-" * 40)
    for chave, valor in metadados.items():
        print(f"{chave}: {valor}")

    if informacoes["previa_textual"]:
        print("\nPrévia textual:")
        print(informacoes["previa_textual"])


def _renomear_documento(biblioteca: BibliotecaDigital) -> None:
    documento_id = input("ID do documento: ").strip()
    novo_nome = input("Novo nome do arquivo, sem extensão obrigatória: ").strip()
    novo_titulo = input("Novo título, opcional: ").strip() or None

    documento = biblioteca.renomear_documento(documento_id, novo_nome, novo_titulo)
    print(f"Documento renomeado com sucesso: {documento['arquivo']}")


def _remover_documento(biblioteca: BibliotecaDigital) -> None:
    documento_id = input("ID do documento: ").strip()
    confirmar = input("Confirma remoção? Digite SIM: ").strip().upper()

    if confirmar != "SIM":
        print("Operação cancelada.")
        return

    if biblioteca.remover_documento(documento_id):
        print("Documento removido com sucesso.")
    else:
        print("Documento não encontrado.")


def _listar_diretorios(biblioteca: BibliotecaDigital) -> None:
    diretorios = biblioteca.listar_diretorios_sistema()

    if not diretorios:
        print("Nenhum diretório encontrado.")
        return

    for diretorio in diretorios:
        print(f"- {diretorio.name}")


def _criar_diretorio(biblioteca: BibliotecaDigital) -> None:
    nome = input("Nome do novo diretório: ").strip()
    caminho = biblioteca.criar_diretorio_sistema(nome)
    print(f"Diretório criado/verificado: {caminho}")


def _remover_diretorio(biblioteca: BibliotecaDigital) -> None:
    nome = input("Nome do diretório a remover: ").strip()
    forcar = input("Forçar remoção se houver conteúdo? [s/N]: ").strip().lower() == "s"

    if biblioteca.remover_diretorio_sistema(nome, forcar=forcar):
        print("Diretório removido com sucesso.")
    else:
        print("Diretório não encontrado.")


def _listar_por_tipo(biblioteca: BibliotecaDigital) -> None:
    agrupado = biblioteca.listar_por_tipo()

    if not agrupado:
        print("Nenhum documento cadastrado.")
        return

    for extensao, documentos in agrupado.items():
        print(f"\nTipo {extensao}:")
        for documento in documentos:
            _imprimir_resumo(documento)


def _listar_por_ano(biblioteca: BibliotecaDigital) -> None:
    agrupado = biblioteca.listar_por_ano()

    if not agrupado:
        print("Nenhum documento cadastrado.")
        return

    for ano, documentos in agrupado.items():
        print(f"\nAno {ano}:")
        for documento in documentos:
            _imprimir_resumo(documento)


def _imprimir_resumo(documento: dict) -> None:
    print(
        f"[{documento['id']}] {documento['titulo']} | "
        f"{documento['ano_publicacao']} | {documento['extensao']} | "
        f"{documento['caminho']}"
    )
