import os
def get_file_size(filename):
        return os.path.getsize(filename)
numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])