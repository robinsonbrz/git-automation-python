ref_arquivo = open("emojis.txt", "r", encoding="utf8")
#linha = ref_arquivo.readline()

lista_de_linhas = ref_arquivo.readlines()
ref_arquivo.close()

print(lista_de_linhas[1])


arquivo_branch_atual = open("acumulador_branches.txt", "r")
branch_atual = arquivo_branch_atual.readlines()
print(int(branch_atual[0]))
arquivo_branch_atual.close()


with open('acumulador_branches.txt', 'w') as arquivo:
    arquivo.write('3')
    arquivo.close()
