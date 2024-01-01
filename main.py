import random
print(random.randint(0, 100))
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)