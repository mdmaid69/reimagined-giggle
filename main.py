import os
print(os.getcwd())
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)