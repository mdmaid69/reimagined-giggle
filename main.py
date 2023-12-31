n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])
import os
def list_files_in_directory(path):
        return os.listdir(path)