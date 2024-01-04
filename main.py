import sys
print(sys.version)
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)