import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
n = 10
print("Cube numbers:", [x**3 for x in range(n)])