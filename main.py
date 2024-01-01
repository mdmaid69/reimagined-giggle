for i in range(5):
        print(i)
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)