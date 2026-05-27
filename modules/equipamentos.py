import json
import os
from modules.validacoes import validar_vinculo_usina

# Caminho para persistência em JSON
caminho_equipamentos = os.path.join(
    os.path.dirname(__file__),
    "..",
    "data",
    "equipamentos.json"
)

equipamentos = {}

def carregar_equipamentos():
    global equipamentos
    if os.path.exists(caminho_equipamentos):
        try:
            with open(caminho_equipamentos, "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
                if isinstance(dados, dict):
                    # Como JSON salva chaves como string, convertemos de volta para int
                    equipamentos = {int(k): v for k, v in dados.items()}
                else:
                    equipamentos = {}
        except Exception as e:
            print(f"⚠️ Erro ao carregar equipamentos: {e}")

def salvar_equipamentos():
    try:
        os.makedirs(os.path.dirname(caminho_equipamentos), exist_ok=True)
        with open(caminho_equipamentos, "w", encoding="utf-8") as arquivo:
            json.dump(equipamentos, arquivo, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"⚠️ Erro ao salvar equipamentos: {e}")

# Carrega os equipamentos ao importar o módulo
carregar_equipamentos()

def cadastro_equipamentos():
    print("==== CADASTRO DE EQUIPAMENTOS ====")
    try:
        id = int(input("Digite a ID do equipamento: "))
    except ValueError:
        print("❌ ID inválido!")
        return

    if id in equipamentos:
        print("❌ Equipamento já cadastrado!")
        return

    try:
        usina = int(input("Digite o ID da usina vinculada: "))
    except ValueError:
        print("❌ ID de usina inválido!")
        return

    # Validação obrigatória da usina usando a função do Arthur
    if not validar_vinculo_usina(usina):
        return

    equipamentos[id] = { 
        "Nome do equipamento": input("Digite o nome do equipamento: "),
        "Tipo do equipamento": input("Digite o tipo do equipamento: "),
        "Fabricante": input("Digite o fabricante: "),
        "Modelo": input("Digite o modelo do equipamento: "),
        "Data": input("Digite a data de instalação: "),
        "Status": input("Digite o status do equipamento: "),
        "Usina vinculada": usina
    }
    
    salvar_equipamentos()
    print("✅ Equipamento cadastrado!")

def visualizar_equipamentos():
    if not equipamentos:
        print("⚠️ Nenhum equipamento cadastrado!")
        return
    for id, dados in equipamentos.items():
        print(f"\nID: {id}")
        for chave, valor in dados.items():
            print(f"{chave}: {valor}")

def editar_equipamento():
    print("\n⚠️ Função de edição de equipamento ainda não implementada (Responsável: Arthur).\n")

def excluir_equipamento():
    print("\n⚠️ Função de exclusão de equipamento ainda não implementada (Responsável: Arthur).\n")


