import json
import os

# Caminho para persistência em JSON
caminho_usinas = os.path.join(
    os.path.dirname(__file__),
    "..",
    "data",
    "usinas.json"
)

# Valor inicial padrão caso o arquivo não exista
usinas = [
    {
        "id": 1,
        "nome": "Solar Nordeste",
        "empresa": "Energia BR",
        "cidade": "Natal",
        "estado": "RN",
        "potencia": 500.0,
        "ID da usina": 1,
        "Nome da usina": "Solar Nordeste",
        "Empresa responsável pela usina": "Energia BR",
        "Cidade da usina": "Natal",
        "UF da usina": "RN",
        "Potência da usina (kWp)": 500.0,
        "Quantidade de painéis": 1200,
        "Data de instalação": "01/01/2025",
        "Status da usina": "ATIVA"
    }
]

def salvar_usinas_json(dados):
    try:
        # Garante que a pasta pai exista
        os.makedirs(os.path.dirname(caminho_usinas), exist_ok=True)
        with open(caminho_usinas, "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)
    except Exception as e:
        print(f"⚠️ Erro ao salvar usinas: {e}")

def carregar_usinas():
    global usinas
    if os.path.exists(caminho_usinas):
        try:
            with open(caminho_usinas, "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
                
                # Se for um dicionário único (como o usinas.json padrão), transforma em lista
                if isinstance(dados, dict):
                    lista_dados = [dados]
                elif isinstance(dados, list):
                    lista_dados = dados
                else:
                    lista_dados = []
                
                normalizados = []
                for item in lista_dados:
                    # Garante que chaves em inglês existam a partir das chaves em português
                    id_val = item.get("id") or item.get("ID da usina")
                    nome_val = item.get("nome") or item.get("Nome da usina")
                    empresa_val = item.get("empresa") or item.get("Empresa responsável pela usina")
                    cidade_val = item.get("cidade") or item.get("Cidade da usina")
                    estado_val = item.get("estado") or item.get("UF da usina")
                    potencia_val = item.get("potencia") or item.get("Potência da usina (kWp)")
                    
                    if id_val is not None:
                        item["id"] = int(id_val)
                        item["ID da usina"] = int(id_val)
                    if nome_val is not None:
                        item["nome"] = str(nome_val)
                        item["Nome da usina"] = str(nome_val)
                    if empresa_val is not None:
                        item["empresa"] = str(empresa_val)
                        item["Empresa responsável pela usina"] = str(empresa_val)
                    if cidade_val is not None:
                        item["cidade"] = str(cidade_val)
                        item["Cidade da usina"] = str(cidade_val)
                    if estado_val is not None:
                        item["estado"] = str(estado_val)
                        item["UF da usina"] = str(estado_val)
                    if potencia_val is not None:
                        item["potencia"] = float(potencia_val)
                        item["Potência da usina (kWp)"] = float(potencia_val)
                        
                    normalizados.append(item)
                
                if normalizados:
                    usinas = normalizados
        except Exception as e:
            print(f"⚠️ Erro ao carregar usinas: {e}")

# Carrega as usinas salvas ao importar o módulo
carregar_usinas()

# Funções de Sérgio - Cadastro de Usinas (Parte 1)
def cadastrar_usina():
    print("==== CADASTRO DE USINA ====")
    try:
        id_usina = int(input("ID da usina: "))
    except ValueError:
        print("❌ ID inválido!")
        return {}

    # Verifica se já existe
    for u in usinas:
        if u["id"] == id_usina:
            print("❌ Usina com este ID já cadastrada!")
            return {}

    salvar_usinas = {}
    salvar_usinas["ID da usina"] = id_usina
    salvar_usinas["Nome da usina"] = input("Nome da usina: ").title()
    salvar_usinas["Empresa responsável pela usina"] = input("Empresa responsável pela usina: ").title()
    salvar_usinas["Cidade da usina"] = input("Cidade da usina: ").title()
    salvar_usinas["UF da usina"] = input("UF da usina: ").upper().strip()
    
    try:
        salvar_usinas["Potência da usina (kWp)"] = float(input("Potência da usina (kWp): "))
    except ValueError:
        print("❌ Potência inválida! Definindo como 0.0")
        salvar_usinas["Potência da usina (kWp)"] = 0.0

    try:
        salvar_usinas["Quantidade de painéis"] = int(input("Quantidade de painéis: "))
    except ValueError:
        print("❌ Quantidade inválida! Definindo como 0")
        salvar_usinas["Quantidade de painéis"] = 0

    salvar_usinas["Data de instalação"] = input("Data de instalação: ").strip()
    salvar_usinas["Status da usina"] = input("Status da usina: ").upper()

    # Mapeia as chaves correspondentes para manter a compatibilidade
    salvar_usinas["id"] = salvar_usinas["ID da usina"]
    salvar_usinas["nome"] = salvar_usinas["Nome da usina"]
    salvar_usinas["empresa"] = salvar_usinas["Empresa responsável pela usina"]
    salvar_usinas["cidade"] = salvar_usinas["Cidade da usina"]
    salvar_usinas["estado"] = salvar_usinas["UF da usina"]
    salvar_usinas["potencia"] = salvar_usinas["Potência da usina (kWp)"]

    # Adiciona à lista global e salva no arquivo JSON
    usinas.append(salvar_usinas)
    salvar_usinas_json(usinas)

    print("=========== CADASTRO DA USINA =========== ")
    print(salvar_usinas["ID da usina"])
    print(salvar_usinas["Nome da usina"])
    print(salvar_usinas["Empresa responsável pela usina"])
    print(salvar_usinas["Cidade da usina"])
    print(salvar_usinas["UF da usina"])
    print(f"{salvar_usinas['Potência da usina (kWp)']}")
    print(salvar_usinas["Quantidade de painéis"])
    print(salvar_usinas["Data de instalação"])
    print(salvar_usinas["Status da usina"])

    print("✅ Usina cadastrada com sucesso!")
    return salvar_usinas 

def listar_usinas():
    print("=========== LISTA DE USINAS =========== ")
    if not usinas:
        print("⚠️ Nenhuma usina cadastrada!")
        return
    for usina in usinas:
        print(f"ID: {usina['id']}")
        print(f"Nome: {usina['nome']}")
        print(f"Empresa: {usina['empresa']}")
        print(f"Cidade: {usina['cidade']}")
        print(f"Estado: {usina['estado']}")
        print(f"Potência: {usina['potencia']} kWp")
        print("=" * 40)

# Funções de Camillo - Edição e Exclusão (Parte 2)
def editar_usina():
    try:
        id_editar = int(input("Digite o ID da usina que deseja editar: "))
    except ValueError:
        print("❌ ID inválido!")
        return

    for usina in usinas:
        if usina["id"] == id_editar:
            print("\nUsina encontrada!")
            usina["nome"] = input("Novo nome: ")
            usina["empresa"] = input("Nova empresa: ")
            usina["cidade"] = input("Nova cidade: ")
            usina["estado"] = input("Novo estado: ")
            
            try:
                usina["potencia"] = float(input("Nova potência: "))
            except ValueError:
                print("❌ Potência inválida! Mantendo o valor anterior.")

            # Mantém as chaves em português sincronizadas
            usina["Nome da usina"] = usina["nome"]
            usina["Empresa responsável pela usina"] = usina["empresa"]
            usina["Cidade da usina"] = usina["cidade"]
            usina["UF da usina"] = usina["estado"]
            usina["Potência da usina (kWp)"] = float(usina["potencia"])

            # Salva as atualizações no JSON
            salvar_usinas_json(usinas)
            print("\nUsina editada com sucesso!")
            return
            
    print("❌ Nenhuma usina encontrada com esse ID.")

def excluir_usina():
    resposta = input("\nDeseja excluir alguma usina? (S/N): ")

    if resposta.upper() == "S":
        try:
            id_excluir = int(input("Digite o ID da usina que deseja excluir: "))
        except ValueError:
            print("❌ ID inválido!")
            return

        for usina in usinas:
            if usina["id"] == id_excluir:
                confirmacao = input("Tem certeza que deseja excluir? (S/N): ")

                if confirmacao.upper() == "S":
                    usinas.remove(usina)
                    # Salva a lista atualizada no JSON
                    salvar_usinas_json(usinas)
                    print("✅ Usina excluída com sucesso!")
                    return
                else:
                    print("Exclusão cancelada.")
                    return
        print("❌ Nenhuma usina encontrada com esse ID.")
    else:
        print("Exclusão cancelada.")


listar_usinas()

