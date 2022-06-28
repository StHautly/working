from git import *
from datetime import datetime as dt
import os

x = dt.now().isoformat()


host = r"C:\Users\Administrador\github\working"
def git_push():
    try:
        repo = Repo(host)
        repo.git.add(update=True)
        repo.index.commit(x)
        origin = repo.remote(name='origin')
        origin.pull()
        origin.push()
    except:
        print('Some error occured while pushing the code')

git_push()
