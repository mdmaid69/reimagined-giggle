import random
print(random.randint(0, 100))
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)