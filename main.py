def greet(name):
        print(f"Hello, {name}!")
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)