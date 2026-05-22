<<<<<<< HEAD
usinas = [
    {
        "id": 1,
        "nome": "Solar Nordeste",
        "empresa": "Energia BR",
        "cidade": "Natal",
        "estado": "RN",
        "potencia": 500
    }
]

id_editar = int(input("Digite o ID da usina que deseja editar: "))

for usina in usinas:

    if usina["id"] == id_editar:

        print("\nUsina encontrada!")

        usina["nome"] = input("Novo nome: ")
        usina["empresa"] = input("Nova empresa: ")
        usina["cidade"] = input("Nova cidade: ")
        usina["estado"] = input("Novo estado: ")
        usina["potencia"] = int(input("Nova potência: "))

        print("\nUsina editada com sucesso!")

resposta = input("\nDeseja excluir alguma usina? (S/N): ")

if resposta.upper() == "S":

    id_excluir = int(input("Digite o ID da usina que deseja excluir: "))

    for usina in usinas:

        if usina["id"] == id_excluir:

            confirmacao = input("Tem certeza que deseja excluir? (S/N): ")

            if confirmacao.upper() == "S":
                usinas.remove(usina)
                print("Usina excluída com sucesso!")

            else:
                print("Exclusão cancelada.")

else:
    print("Exclusão cancelada.")
=======
import json
import os

def cadastrar_usina():
    salvar_usinas = {}

    salvar_usinas["ID da usina"] =  int(input("ID da usina: "))

    salvar_usinas["Nome da usina"] = input("Nome da usina: ").capitalize()
    
    salvar_usinas["Empresa responsável pela usina"] = input("Empresa responsável pela usina: ").capitalize()

    salvar_usinas["Cidade da usina"] = input("Cidade da usina: ").capitalize()

    salvar_usinas["UF da usina"] = input("UF da usina: ").upper().strip()

    salvar_usinas["Potência da usina (kWp)"] = float(input("Potência da usina (kWp): "))

    salvar_usinas["Quantidade de painéis"] = int(input("Quantidade de painéis: "))

    salvar_usinas["Data de instalação"] = input("Data de instalação: ").strip()
  
    salvar_usinas["Status da usina"] = input("Status da usina: ").upper()   

    return salvar_usinas 

def salvar_usinas_json(dados):

    caminho = os.path.join(
        os.path.dirname(__file__),
        "..",
        "data",
        "usinas.json"
    )

    with open(caminho, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent = 4, ensure_ascii=False)

usina = cadastrar_usina()
salvar_usinas_json(usina)

def listar_usinas():
    print("=========== LISTA DE USINAS =========== ")
    print(usina["ID da usina"])
    print(usina["Nome da usina"])
    print(usina["Empresa responsável pela usina"])
    print(usina["Cidade da usina"])
    print(usina["UF da usina"])
    print(f"{usina["Potência da usina (kWp)"]}")
    print(usina["Quantidade de painéis"])
    print(usina["Data de instalação"])
    print(usina["Status da usina"])
    print("=======================================")
>>>>>>> 298c3e9 (fiz a base do cadastro (tentando dnv, pq antes n foi))
