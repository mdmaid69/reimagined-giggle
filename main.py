import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
n = 10
print("Powers of 2:", [2**x for x in range(n)])