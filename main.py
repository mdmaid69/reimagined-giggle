from collections import Counter
print(Counter("hello world"))
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)