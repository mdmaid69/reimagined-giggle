import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
text = "Hello, world!"
print("Uppercase:", text.upper())