

print("==== CADASTRO DE EQUIPAMENTOS ====")

equipamentos={}
usinas={}

def cadastro_equipamentos():
   id=int(input("digite a id do equipamento: "))
   if id in equipamentos:
      print(" equipamento já cadastrado!")
      return

   equipamentos[id]={ 
      "Nome do equipamento":input("digite o nome do equipamento: "),
      "tipo do equipamento":input("digite o tipo do equipamento: "),
      "fabricante":input("digite o fabricante: "),
      "modelo":input("digite o modelo do equipamento: "),
      "data":input("digite a data de instalação: "),
      "status":input("digite o status do equipamento: ")
   }
   usina=int(input("digite o id da usina vinculada: "))
   if usina  not in usinas:
         print("usina não encontrada!")
         return   

   print("equipamento cadastrado!")


def visualizar_equipamentos():
  if not equipamentos:
    print("nenhum equipamento cadastrado!")
    return
  for id , dados in equipamentos.items():
    print(f"\n ID: {id} ")

  for chave, valor in dados:
     print(f"{chave}: {valor}")

