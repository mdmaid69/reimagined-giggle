import os
def get_file_size(filename):
        return os.path.getsize(filename)
n = 10
print("Cube numbers:", [x**3 for x in range(n)])