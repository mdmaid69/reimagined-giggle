import os
def change_working_directory(path):
        os.chdir(path)
n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])