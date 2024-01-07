print([x**2 for x in range(10)])
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)