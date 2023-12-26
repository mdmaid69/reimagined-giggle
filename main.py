import os
def list_files_in_directory(path):
        return os.listdir(path)
n = 10
print("Square numbers:", [x**2 for x in range(n)])