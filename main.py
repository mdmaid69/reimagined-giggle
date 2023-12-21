import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
numbers = [1, 2, 3, 4, 5]
print("Squared:", [n**2 for n in numbers])