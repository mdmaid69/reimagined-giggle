import os
print(os.getcwd())
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)