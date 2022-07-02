from asyncore import file_dispatcher
from importlib.util import source_hash
import os
path="C:/Users/mrvsv/Downloads/Python_(32bit)_v3.8.1.exe"
root,ext=os.path.splitext(path)
print(dir(os))
os.getcwd()
os.mkdir("vijay")
os.listdir()
os.path.exists("C:/Users/mrvsv/vijay")
import shutil
source="C:/Users/mrvsv/Downloads/heic_10690.heic"
destination="C:/Users/mrvsv/OneDrive/Documents/img"
shutil.copy(source,destination)
dest=shutil.copy(source,destination)
print("After copying file")
print(os.listdir(path))
