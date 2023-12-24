text = "Hello, world!"
print("Characters:", len(text))
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)