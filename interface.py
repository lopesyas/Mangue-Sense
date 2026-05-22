# ==========================
# MANGUE SENSE
# Interface do Sistema
# ==========================


def sucesso():
    print("\n Operação realizada com sucesso!")


def erro():
    print("\n Ocorreu um erro.")


def campo_invalido():
    print("\n Entrada inválida. Tente novamente.")


# ------------------------
# MENU USINAS
# ------------------------

def menu_usinas():

    while True:

        print("\n========== USINAS ==========")

        print("1 - Cadastrar Usina")
        print("2 - Listar Usinas")
        print("3 - Editar Usina")
        print("4 - Excluir Usina")
        print("5 - Voltar")

        escolha = input("\nEscolha: ")

        if escolha == "1":
            print("Cadastro de usina")
            sucesso()

        elif escolha == "2":
            print("Lista de usinas")
            sucesso()

        elif escolha == "3":
            print("Editar usina")
            sucesso()

        elif escolha == "4":
            print("Excluir usina")
            sucesso()

        elif escolha == "5":
            break

        else:
            campo_invalido()


# ------------------------
# MENU EQUIPAMENTOS
# ------------------------

def menu_equipamentos():

    while True:

        print("\n======= EQUIPAMENTOS =======")

        print("1 - Cadastrar Equipamento")
        print("2 - Listar Equipamentos")
        print("3 - Editar Equipamento")
        print("4 - Excluir Equipamento")
        print("5 - Voltar")

        escolha = input("\nEscolha: ")

        if escolha == "1":
            print("Cadastro equipamento")
            sucesso()

        elif escolha == "2":
            print("Lista equipamentos")
            sucesso()

        elif escolha == "3":
            print("Editar equipamento")
            sucesso()

        elif escolha == "4":
            print("Excluir equipamento")
            sucesso()

        elif escolha == "5":
            break

        else:
            campo_invalido()


# ------------------------
# MENU PRINCIPAL
# ------------------------

while True:

    print("\n================================")
    print("          MANGUE SENSE")
    print("================================")

    print("1 - Gerenciar Usinas")
    print("2 - Gerenciar Equipamentos")
    print("3 - Visualizar Alertas")
    print("4 - Sair")

    opcao = input("\nEscolha uma opção: ")

    if opcao == "1":
        menu_usinas()

    elif opcao == "2":
        menu_equipamentos()

    elif opcao == "3":
        print("\nNenhum alerta disponível")

    elif opcao == "4":
        print("\nSistema encerrado.")
        break

    else:
        campo_invalido()
