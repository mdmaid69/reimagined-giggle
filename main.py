import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
n = 10
print("Cube numbers:", [x**3 for x in range(n)])