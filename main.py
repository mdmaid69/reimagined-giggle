import os
def list_files_in_directory(path):
        return os.listdir(path)
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])