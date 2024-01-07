numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)