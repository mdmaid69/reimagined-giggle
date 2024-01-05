import os
def list_files_in_directory(path):
        return os.listdir(path)
numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])