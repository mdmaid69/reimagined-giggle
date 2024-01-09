import os
print(os.getcwd())
import shutil
def delete_directory(path):
        shutil.rmtree(path)