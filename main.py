import os
def list_files_in_directory(path):
        return os.listdir(path)
n = 10
print("Powers of 2:", [2**x for x in range(n)])