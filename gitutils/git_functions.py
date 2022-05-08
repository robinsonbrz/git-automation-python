# -*- coding: utf-8 -*-
"""
Created on Sat May  7 11:20:38 2022

@author: Robinson
"""

import os

import git

import le_txt

# rorepo is a Repo instance pointing to the git-python repository.
# For all you know, the first argument to Repo is a path to the repository
# you want to work with


def print_repos():
    print("#########################")
    print("repo:   ", repo)
    print("branch: ", branch)
    print("#########################\n")


def get_branch():
    repo = git.Repo(".")
    branch = repo.active_branch
    return branch


def get_repo():
    repo = git.Repo(".")
    return repo


def checkout_branch(nome_branch):# faz checout em um branch criado
    get_branch()
    repo.git.checkout(nome_branch)


#(nome_novo_branch):
######## Cria um novo branch
def create_new_branch(nome_novo_branch):     
    print(nome_novo_branch)
    comando = "git checkout -b " + nome_novo_branch
    os.system(comando)
    return


def push_batch(comentario_commmit):
    nome_branch_atual = get_branch()
    print("\n\n\n\n\n")


    numero_branch_atual = le_txt.get_branch_atual()
    emoji_atual = le_txt.get_emoji(numero_branch_atual) + " "


    os.system("git add .")
    
    comando = 'git commit -m "' + emoji_atual[0:-2] + ' ' + comentario_commmit + '"'
    print(comando)
    os.system(comando)
    
    comando = "git checkout main"
    os.system(comando)

    comando = "git rebase " + str(nome_branch_atual)
    os.system(comando)

    comando = "git push"
    os.system(comando)

    numero_novo_branch = int(numero_branch_atual) + 1
    nome_novo_branch = "feat" + str(numero_novo_branch)
    create_new_branch(nome_novo_branch)

    le_txt.set_branch_atual(numero_novo_branch)
    return
    





# bare_repo = Repo.init(os.path.join(rw_dir, 'bare-repo'), bare=True)
# assert bare_repo.bare

#######
# repo.untracked_files             # retrieve a list of untracked files
#######


######## Cria um novo branch
# new_branch = repo.create_head('novobranch2')               # create a new branch ...


# print_repos()

# print("Criando um novo branch")


# recupera a informação do repositorio local atualizado

'''
repo = git.Repo("../")
branch = repo.active_branch

print_repos()


repo.git.add(update=True)

'''
# index = repo.index
# index.add("*")




