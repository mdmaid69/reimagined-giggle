import os
def remove_directory(path):
        os.rmdir(path)
n = 10
print("Powers of 2:", [2**x for x in range(n)])