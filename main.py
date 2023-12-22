import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
def greet(name):
        print(f"Hello, {name}!")