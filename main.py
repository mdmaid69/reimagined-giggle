import os
def change_working_directory(path):
        os.chdir(path)
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)