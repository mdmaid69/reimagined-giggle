import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
n = 10
print("Square numbers:", [x**2 for x in range(n)])