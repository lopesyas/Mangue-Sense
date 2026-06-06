

import json
import os


caminho_equipamentos = os.path.join(os.path.dirname(__file__), "..", "data", "equipamentos.json")
caminho_usinas       = os.path.join(os.path.dirname(__file__), "..", "data", "usinas.json")



def carregar_json(caminho):
    if not os.path.exists(caminho):
        return []
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            dados = json.load(f)
            # Normaliza: se o JSON contém um único objeto (dict), transforma em lista [dict]
            if isinstance(dados, list):
                return dados
            if isinstance(dados, dict):
                return [dados]
            return []
    except Exception as e:
        print(f"Erro ao carregar {caminho}: {e}")
        return []


def salvar_equipamentos(equipamentos):
    try:
        os.makedirs(os.path.dirname(caminho_equipamentos), exist_ok=True)
        with open(caminho_equipamentos, "w", encoding="utf-8") as f:
            json.dump(equipamentos, f, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"Erro ao salvar equipamentos: {e}")



def registrar_dados_operacionais():
    usinas = carregar_json(caminho_usinas)
    if not usinas:
        print("Nenhuma usina cadastrada. Cadastre uma usina primeiro.")
        return

    print("\n==== DADOS OPERACIONAIS ====")
    print("Usinas disponíveis:")
    for u in usinas:
        print(f"  ID {u['id']} - {u['nome']} ({u['cidade']}/{u['estado']})")

    try:
        id_usina = int(input("\nID da usina: "))
    except ValueError:
        print("ID invalido.")
        return

    usina = next((u for u in usinas if u["id"] == id_usina), None)
    if not usina:
        print("Usina nao encontrada.")
        return

    try:
        temperatura = float(input("Temperatura atual (C): "))
        geracao     = float(input("Geracao atual (kWh): "))
        if geracao < 0:
            print("Geracao nao pode ser negativa.")
            return
        desempenho = int(input("Desempenho (0 a 100): "))
        if not (0 <= desempenho <= 100):
            print("Desempenho fora do intervalo.")
            return
    except ValueError:
        print("Valor invalido.")
        return

    dados = {
        "id_usina":    id_usina,
        "nome_usina":  usina["nome"],
        "temperatura": temperatura,
        "geracao":     geracao,
        "desempenho":  desempenho,
    }

    print(f"\nDados operacionais da usina '{usina['nome']}' registrados.")
    return dados  



def cadastrar_equipamento():
    equipamentos = carregar_json(caminho_equipamentos)
    usinas       = carregar_json(caminho_usinas)

    if not usinas:
        print("Nenhuma usina cadastrada. Cadastre uma usina primeiro.")
        return

    print("\n==== CADASTRO DE EQUIPAMENTO ====")

    try:
        id_eq = int(input("ID do equipamento: "))
    except ValueError:
        print("ID invalido.")
        return

    if any(e["id"] == id_eq for e in equipamentos):
        print("Equipamento ja cadastrado.")
        return

    nome      = input("Nome do equipamento: ").strip()
    tipo      = input("Tipo do equipamento: ").strip()
    fabricante = input("Fabricante: ").strip()
    modelo    = input("Modelo: ").strip()
    data      = input("Data de instalacao: ").strip()
    status    = input("Status: ").upper().strip()

    print("\nUsinas disponiveis:")
    for u in usinas:
        print(f"  ID {u['id']} - {u['nome']} ({u['cidade']}/{u['estado']})")

    try:
        id_usina = int(input("ID da usina vinculada: "))
    except ValueError:
        print("ID invalido.")
        return

    usina = next((u for u in usinas if u["id"] == id_usina), None)
    if not usina:
        print("Usina nao encontrada.")
        return

    equipamento = {
        "id":          id_eq,
        "nome":        nome,
        "tipo":        tipo,
        "fabricante":  fabricante,
        "modelo":      modelo,
        "data":        data,
        "status":      status,
        "id_usina":    id_usina,
        "nome_usina":  usina["nome"],
    }

    equipamentos.append(equipamento)
    salvar_equipamentos(equipamentos)
    print(f"Equipamento '{nome}' cadastrado e vinculado a '{usina['nome']}'.")


def visualizar_equipamentos():
    equipamentos = carregar_json(caminho_equipamentos)

    if not equipamentos:
        print("Nenhum equipamento cadastrado.")
        return

    print("\n==== EQUIPAMENTOS CADASTRADOS ====")
    for eq in equipamentos:
        print(f"\n  ID:         {eq['id']}")
        print(f"  Nome:       {eq['nome']}")
        print(f"  Tipo:       {eq['tipo']}")
        print(f"  Fabricante: {eq['fabricante']}")
        print(f"  Modelo:     {eq['modelo']}")
        print(f"  Data:       {eq['data']}")
        print(f"  Status:     {eq['status']}")
        print(f"  Usina:      {eq['nome_usina']} (ID {eq['id_usina']})")



def menu_equipamentos():
    while True:
        print("\n==== EQUIPAMENTOS ====")
        print("[1] Registrar dados operacionais da usina")
        print("[2] Cadastrar equipamento")
        print("[3] Visualizar equipamentos")
        print("[4] Sair")

        try:
            opcao = int(input("Opcao: "))
        except ValueError:
            print("Opcao invalida.")
            continue

        if opcao == 1:
            registrar_dados_operacionais()
        elif opcao == 2:
            cadastrar_equipamento()
        elif opcao == 3:
            visualizar_equipamentos()
        elif opcao == 4:
            print("Saindo.")
            break
        else:
            print("Opcao invalida.")


if __name__ == "__main__":
    menu_equipamentos()


# Compatibilidade com outras partes da interface que importam
# Nota: unificamos a API para `cadastrar_equipamento` (singular).
# Se outras partes do código ainda importarem o nome antigo,
# mantemos um alias histórico com o nome anterior para compatibilidade.
def cadastro_equipamentos():
    return cadastrar_equipamento()


def editar_equipamento():
    """Stub de edição de equipamento — em desenvolvimento.
    Mantém API para importação e evita ImportError enquanto a feature não
    estiver implementada pelo responsável.
    """
    print("\n⚠️ Função de editar equipamento em desenvolvimento.")
    return None


def excluir_equipamento():
    """Stub de exclusão de equipamento — em desenvolvimento.
    """
    print("\n⚠️ Função de excluir equipamento em desenvolvimento.")
    return None