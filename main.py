n = 10
print("Powers of 2:", [2**x for x in range(n)])
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)