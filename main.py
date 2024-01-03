import sys
print(sys.version)
import shutil
def delete_directory(path):
        shutil.rmtree(path)