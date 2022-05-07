# -*- coding: utf-8 -*-
"""
Created on Sat May  7 11:20:38 2022

@author: Robinson
"""

import git

# rorepo is a Repo instance pointing to the git-python repository.
# For all you know, the first argument to Repo is a path to the repository
# you want to work with


def print_repos():
    print("#########################")
    print("repo:   ", repo)
    print("branch: ", branch)
    print("#########################\n")


repo = git.Repo("../")
branch = repo.active_branch

# bare_repo = Repo.init(os.path.join(rw_dir, 'bare-repo'), bare=True)
# assert bare_repo.bare

#######
# repo.untracked_files             # retrieve a list of untracked files
#######

print("inicio do dia")
print_repos()

######## Cria um novo branch
# new_branch = repo.create_head('novobranch2')               # create a new branch ...


# print_repos()

# print("Criando um novo branch")
# faz checout em um branch criado
repo.git.checkout("main")

# recupera a informação do repositorio local atualizado
repo = git.Repo("../")
branch = repo.active_branch

print_repos()


index = repo.index
index.add("*")



# Commit the changes to deviate masters history
repo.index.commit("Commit efetuado pelo script Python")
