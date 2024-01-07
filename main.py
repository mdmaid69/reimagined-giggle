text = "Hello, world!"
print("Uppercase:", text.upper())
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)