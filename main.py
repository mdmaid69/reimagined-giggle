import os
def list_files_in_directory(path):
        return os.listdir(path)
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b