import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
name = "Python"
print("Hello,", name)