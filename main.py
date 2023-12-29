import os
def list_files_in_directory(path):
        return os.listdir(path)
n = 10
print("Cube numbers:", [x**3 for x in range(n)])