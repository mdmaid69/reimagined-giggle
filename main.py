import os
def remove_directory(path):
        os.rmdir(path)
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b