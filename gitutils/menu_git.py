import git_functions

print("Menu de opções Git\n")
print("S -Ver STATUS")
print("B -Ver BRANCH atual")
print("C -cria BRANCH e checkout")
print('P -Lote de comandos, "add .", "Commit","Checkout main","rebase","Push origin main"')

selecao = input("Digite sua opção: ").upper()

if selecao == "B":
    print(git_functions.get_branch())
elif selecao == "C":
    nome_novo_branch = input("Digite o nome do novo branch: ")
    print(git_functions.create_new_branch(nome_novo_branch))
elif selecao == "P":
    comentario_commmit = input("Digite mensagem de commit: ")
    git_functions.push_batch(comentario_commmit)
