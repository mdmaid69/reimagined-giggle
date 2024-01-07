n = 10
print("Square numbers:", [x**2 for x in range(n)])
import os
def get_file_size(filename):
        return os.path.getsize(filename)