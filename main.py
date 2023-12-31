for i in range(5):
        print(i)
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)