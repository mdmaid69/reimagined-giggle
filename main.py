import os
def remove_directory(path):
        os.rmdir(path)
n = 10
print("Cube numbers:", [x**3 for x in range(n)])