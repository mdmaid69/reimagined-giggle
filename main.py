import os
def list_files_in_directory(path):
        return os.listdir(path)
numbers = [1, 2, 3, 4, 5]
print("Squared:", [n**2 for n in numbers])