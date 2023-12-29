for i in range(5):
        print(i)
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)