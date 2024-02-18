def adicionar_contato(contatos, nome, telefone, email):
  contato = {
    "nome": nome,
    "telefone": telefone,
    "email": email,
    "Favorito": False
  }
  contatos.append(contato)
  print(f"\nContato de {nome} adicionado a agenda com sucesso!")
  return

def ver_contato(contatos):
  print("\nContatos da agenda: ")
  for indice, contato in enumerate(contatos, start=1):
    favorito = "✓" if contato["Favorito"] else " "
    nome_contato = contato["nome"]
    telefone_contato = contato["telefone"]
    email_contato = contato["email"]
    print(f"{indice} -> [{favorito}] {nome_contato} - {telefone_contato} - {email_contato}\n")

def editar_contato(contatos, indice_contato, novo_nome, novo_telefone, novo_email):
  indice_contato_ajustado = int(indice_contato) - 1
  if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
    contatos[indice_contato_ajustado]["nome"] = novo_nome
    contatos[indice_contato_ajustado]["telefone"] = novo_telefone
    contatos[indice_contato_ajustado]["email"] = novo_email
  else:
    print("Indice de contato inválido.")
  return

def favoritar_contato(contatos, indice_contato):
  indice_contato_ajustado = int(indice_contato) - 1
  if contatos[indice_contato_ajustado]["Favorito"] == False:
    contatos[indice_contato_ajustado]["Favorito"] = True
    print(f"\nContato {indice_contato} marcado como favorito!")
  else: 
    contatos[indice_contato_ajustado]["Favorito"] = False
    print(f"\nContato {indice_contato} desmarcado de favorito!")
  return

def ver_contato_favorito(contatos):
  print("\nContatos Favoritos: ")
  for indice, contato in enumerate(contatos, start=1):
    if contato["Favorito"] == True:
      favorito = "✓" if contato["Favorito"] else " "
      nome_contato = contato["nome"]
      telefone_contato = contato["telefone"]
      email_contato = contato["email"]
      print(f"{indice} --> [{favorito}] {nome_contato} - {telefone_contato} - {email_contato}\n")
  return

def deletar_contato(contatos, indice_contato):
  indice_contato_ajustado = int(indice_contato) - 1
  if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
    contato = contatos[indice_contato_ajustado]
    contatos.remove(contato)
  return


contatos = []
while True:
  print("MENU DE OPÇÕES DA AGENDA: ")
  print("1. Adicionar um contato.")
  print("2. Ver contatos cadastrados.")
  print("3. Editar contato.")
  print("4. Marcar/desmarcar contato com favorito.")
  print("5. Ver lista de contatos favoritos.")
  print("6. Apagar contato.")
  print("7. Sair da Agenda.")

  escolha = input("\n---> Escolha uma opção: ")

  if escolha == "1":
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o número: ")
    email = input("Digite o email: ")
    adicionar_contato(contatos, nome, telefone, email)

  elif escolha == "2":
    ver_contato(contatos)

  elif escolha == "3":
    ver_contato(contatos)
    indice_contato = input("Digite o indice do contato que gostaria de editar: ")
    novo_nome = input("Digite o novo nome: ")
    novo_telefone = input("Digite o novo número: ")
    novo_email = input("Digite o novo email: ")
    editar_contato(contatos, indice_contato, novo_nome, novo_telefone, novo_email)

  elif escolha == "4":
    ver_contato(contatos)
    indice_contato = input("Digite o número do contato que deseja marcar/desmarcar como favorito: ")
    favoritar_contato(contatos, indice_contato)

  elif escolha == "5":
    ver_contato_favorito(contatos)

  elif escolha == "6":
    ver_contato(contatos)
    indice_contato = input("Digite o número do contato que deseja apagar: ")
    deletar_contato(contatos, indice_contato)

  elif escolha == "7":
    break

  else:
    print("\n---> Opção inválida, tente novamente! <---\n")

print("\nSaindo do programa!")