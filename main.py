import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
n = 10
print("Cube numbers:", [x**3 for x in range(n)])