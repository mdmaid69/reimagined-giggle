import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
n = 10
print("Square numbers:", [x**2 for x in range(n)])