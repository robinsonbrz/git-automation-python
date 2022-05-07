# -*- coding: utf-8 -*-
"""
Created on Sat May  7 11:20:38 2022

@author: Max
"""

from git import Repo

# rorepo is a Repo instance pointing to the git-python repository.
# For all you know, the first argument to Repo is a path to the repository
# you want to work with
repo = Repo(self.rorepo.working_tree_dir)
assert not repo.bare


bare_repo = Repo.init(os.path.join(rw_dir, 'bare-repo'), bare=True)
assert bare_repo.bare

