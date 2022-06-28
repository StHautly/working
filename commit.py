from git import *
from datetime import datetime as dt
import os

x = dt.now().isoformat()

host = r"C:\Users\Administrador\github\working"
repo = Repo(host)
repo.git.add(all=True)
repo.index.commit(x)
repo.git.push()
