import os
def change_working_directory(path):
        os.chdir(path)
n = 10
print("Cube numbers:", [x**3 for x in range(n)])