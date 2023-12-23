def greet(name):
        print(f"Hello, {name}!")
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)