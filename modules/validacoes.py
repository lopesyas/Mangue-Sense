import json

with open("usinas.json", "r") as arquivo:
    usinas = json.load(arquivo)

id_editar = input("Digite o ID da usina que deseja editar: ")

if id_editar.isdigit():

    id_editar = int(id_editar)

    for usina in usinas:

        if usina["id"] == id_editar:

            print("\nUsina encontrada!")

            nome = input("Novo nome: ")
            empresa = input("Nova empresa: ")
            cidade = input("Nova cidade: ")
            estado = input("Novo estado: ")
            potencia = input("Nova potência: ")

            if nome == "":
                print("O nome da usina não pode ficar vazio.")

            elif empresa == "":
                print("A empresa não pode ficar vazia.")

            elif cidade == "":
                print("A cidade não pode ficar vazia.")

            elif estado == "":
                print("O estado não pode ficar vazio.")

            elif not potencia.isdigit():
                print("A potência deve ser um número.")

            else:
                usina["nome"] = nome
                usina["empresa"] = empresa
                usina["cidade"] = cidade
                usina["estado"] = estado
                usina["potencia"] = int(potencia)

                print("\nUsina editada com sucesso!")

                with open("usinas.json", "w") as arquivo:
                    json.dump(usinas, arquivo, indent=4)

            break

    else:
        print("Nenhuma usina encontrada com esse ID.")

else:
    print("ID inválido.")

resposta = input("\nDeseja excluir alguma usina? (S/N): ")

if resposta.upper() == "S":

    id_excluir = input("Digite o ID da usina que deseja excluir: ")

    if id_excluir.isdigit():

        id_excluir = int(id_excluir)

        for usina in usinas:

            if usina["id"] == id_excluir:

                confirmacao = input("Tem certeza que deseja excluir? (S/N): ")

                if confirmacao.upper() == "S":
                    usinas.remove(usina)

                    with open("usinas.json", "w") as arquivo:
                        json.dump(usinas, arquivo, indent=4)

                    print("Usina excluída com sucesso!")

                else:
                    print("Exclusão cancelada.")

                break

        else:
            print("Nenhuma usina encontrada com esse ID.")

    else:
        print("ID inválido.")

else:
    print("Exclusão cancelada.")