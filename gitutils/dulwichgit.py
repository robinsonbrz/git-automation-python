from dulwich import porcelain
from dulwich.repo import Repo

git_path = "../"

r = Repo(git_path)
c = r[r.head()]

print("Commit message: ", c)
porcelain.log(git_path, max_entries=1)

