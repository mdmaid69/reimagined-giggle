import os
def change_working_directory(path):
        os.chdir(path)
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))