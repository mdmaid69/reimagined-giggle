import os
def get_file_size(filename):
        return os.path.getsize(filename)
n = 10
print("Powers of 2:", [2**x for x in range(n)])