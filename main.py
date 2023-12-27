text = "Hello, world!"
print("Characters:", len(text))
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)