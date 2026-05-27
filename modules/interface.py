from modules.usinas import cadastrar_usina, listar_usinas, editar_usina, excluir_usina
from modules.equipamentos import cadastro_equipamentos, visualizar_equipamentos, editar_equipamento, excluir_equipamento

def exibir_menu_principal():
    """Menu principal do sistema - Giovana"""
    while True:
        print("\n===================================")
        print("     MANGUE SENSE")
        print("===================================")
        print("1 - Gerenciar Usinas")
        print("2 - Gerenciar Equipamentos")
        print("3 - Visualizar Alertas")
        print("4 - Sair")
        print("===================================")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            menu_usinas()
        elif opcao == "2":
            menu_equipamentos()
        elif opcao == "3":
            print("\n⚠️ Função ainda não implementada.\n")
        elif opcao == "4":
            print("\n👋 Até logo!\n")
            break
        else:
            print("\n❌ Opção inválida. Tente novamente.\n")

def menu_usinas():
    """Menu de gerenciamento de usinas - Giovana"""
    while True:
        print("\n=========== USINAS ===========")
        print("1 - Cadastrar Usina")
        print("2 - Listar Usinas")
        print("3 - Editar Usina")
        print("4 - Excluir Usina")
        print("5 - Voltar")
        print("=============================")
        
        opcao = input("Escolha: ")
        
        if opcao == "1":
            cadastrar_usina()
        elif opcao == "2":
            listar_usinas()
        elif opcao == "3":
            editar_usina()
        elif opcao == "4":
            excluir_usina()
        elif opcao == "5":
            break
        else:
            print("\n❌ Opção inválida.\n")

def menu_equipamentos():
    """Menu de gerenciamento de equipamentos - Giovana"""
    while True:
        print("\n=========== EQUIPAMENTOS ===========")
        print("1 - Cadastrar Equipamento")
        print("2 - Listar Equipamentos")
        print("3 - Editar Equipamento")
        print("4 - Excluir Equipamento")
        print("5 - Voltar")
        print("====================================")
        
        opcao = input("Escolha: ")
        
        if opcao == "1":
            cadastro_equipamentos()
        elif opcao == "2":
            visualizar_equipamentos()
        elif opcao == "3":
            editar_equipamento()
        elif opcao == "4":
            excluir_equipamento()
        elif opcao == "5":
            break
        else:
            print("\n❌ Opção inválida.\n")

