import os
def remove_directory(path):
        os.rmdir(path)
n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])