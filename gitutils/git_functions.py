# -*- coding: utf-8 -*-
"""
Created on Sat May  7 11:20:38 2022

@author: Robinson
"""

import os

import git

import le_txt


def get_branch():
    comando = "git rev-parse --abbrev-ref HEAD"
    os.system(comando + " > tmp")
    retorno = open('tmp', 'r').read()
    os.remove('tmp')
    return retorno


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

    numero_novo_branch = int(numero_branch_atual) + 1
    nome_novo_branch = "feat" + str(numero_novo_branch)
    le_txt.set_branch_atual(numero_novo_branch)

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

    create_new_branch(nome_novo_branch)

    return
