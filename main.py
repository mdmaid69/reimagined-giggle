import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
import time
print(time.time())