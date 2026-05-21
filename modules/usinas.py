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