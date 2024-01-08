import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
def greet(name):
        print(f"Hello, {name}!")