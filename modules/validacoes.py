import json
import os

def validar_vinculo_usina(usina_id):
    """
    [ESBOÇO] Função de validação de vínculo com a usina.
    Responsabilidade: Arthur (Parte 2).
    """
    print("\n⚠️ Validação de vínculo de usina ainda não implementada (Responsável: Arthur).")
    return True

if __name__ == "__main__":
    # Código original dos alunos isolado para evitar bloqueio ao importar
    caminho_usinas_local = "usinas.json"
    if not os.path.exists(caminho_usinas_local):
        caminho_usinas_local = os.path.join(os.path.dirname(__file__), "..", "data", "usinas.json")

    try:
        with open(caminho_usinas_local, "r") as arquivo:
            usinas = json.load(arquivo)
            if not isinstance(usinas, list):
                usinas = [usinas]
    except Exception:
        usinas = []

    id_editar = input("Digite o ID da usina que deseja editar: ")

    if id_editar.isdigit():

        id_editar = int(id_editar)

        for usina in usinas:

            if usina.get("id") == id_editar or usina.get("ID da usina") == id_editar:

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
                    
                    usina["Nome da usina"] = nome
                    usina["Empresa responsável pela usina"] = empresa
                    usina["Cidade da usina"] = cidade
                    usina["UF da usina"] = estado
                    usina["Potência da usina (kWp)"] = float(potencia)

                    print("\nUsina editada com sucesso!")

                    with open(caminho_usinas_local, "w") as arquivo:
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

                if usina.get("id") == id_excluir or usina.get("ID da usina") == id_excluir:

                    confirmacao = input("Tem certeza que deseja excluir? (S/N): ")

                    if confirmacao.upper() == "S":
                        usinas.remove(usina)

                        with open(caminho_usinas_local, "w") as arquivo:
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