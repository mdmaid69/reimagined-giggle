import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
name = "Python"
print("Hello,", name)