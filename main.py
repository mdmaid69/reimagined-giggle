text = "Hello, world!"
print("Reversed:", text[::-1])
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)