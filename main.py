import os
def change_working_directory(path):
        os.chdir(path)
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])