import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
n = 10
print("Square numbers:", [x**2 for x in range(n)])