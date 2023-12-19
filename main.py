import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
def greet(name):
        print(f"Hello, {name}!")