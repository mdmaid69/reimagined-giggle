n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))
import os
def list_files_in_directory(path):
        return os.listdir(path)