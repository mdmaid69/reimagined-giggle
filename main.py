import os
def remove_directory(path):
        os.rmdir(path)
n = 10
print("Square numbers:", [x**2 for x in range(n)])