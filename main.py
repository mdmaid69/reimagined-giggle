import random
print(random.randint(0, 100))
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)