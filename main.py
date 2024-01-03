print([x**2 for x in range(10)])
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)