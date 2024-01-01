n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b
import os
def change_working_directory(path):
        os.chdir(path)