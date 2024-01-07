text = "Hello, world!"
print("Reversed:", text[::-1])
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)