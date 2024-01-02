import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
text = "Hello, world!"
print("Characters:", len(text))