from modules.usinas import cadastrar_usina, listar_usinas, editar_usina, excluir_usina
from modules.equipamentos import cadastro_equipamentos, visualizar_equipamentos


def exibir_menu_principal():
    while True:
        print("\n================================")
        print("          MANGUE SENSE")
        print("================================")
        print("1 - Gerenciar Usinas")
        print("2 - Gerenciar Equipamentos")
        print("3 - Visualizar Alertas")
        print("4 - Sair")

        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == "1":
            menu_usinas()
        elif opcao == "2":
            menu_equipamentos()
        elif opcao == "3":
            print("\nNenhum alerta disponível.")
        elif opcao == "4":
            print("\nSistema encerrado.")
            break
        else:
            print("\nOpção inválida. Tente novamente.")


def menu_usinas():
    while True:
        print("\n========== USINAS ==========")
        print("1 - Cadastrar Usina")
        print("2 - Listar Usinas")
        print("3 - Editar Usina")
        print("4 - Excluir Usina")
        print("5 - Voltar")

        escolha = input("\nEscolha: ").strip()

        if escolha == "1":
            cadastrar_usina()
        elif escolha == "2":
            listar_usinas()
        elif escolha == "3":
            editar_usina()
        elif escolha == "4":
            excluir_usina()
        elif escolha == "5":
            break
        else:
            print("\nEntrada inválida. Tente novamente.")


def menu_equipamentos():
    while True:
        print("\n======= EQUIPAMENTOS =======")
        print("1 - Cadastrar Equipamento")
        print("2 - Listar Equipamentos")
        print("3 - Editar Equipamento")
        print("4 - Excluir Equipamento")
        print("5 - Voltar")

        escolha = input("\nEscolha: ").strip()

        if escolha == "1":
            cadastro_equipamentos()
        elif escolha == "2":
            visualizar_equipamentos()
        elif escolha == "3":
            print("\nFunção de editar equipamento ainda não implementada.")
        elif escolha == "4":
            print("\nFunção de excluir equipamento ainda não implementada.")
        elif escolha == "5":
            break
        else:
            print("\nEntrada inválida. Tente novamente.")


if __name__ == "__main__":
    exibir_menu_principal()

# TESTE_GIT