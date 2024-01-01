text = "Hello, world!"
print("Uppercase:", text.upper())
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)