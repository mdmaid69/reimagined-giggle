n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])
import os
def remove_directory(path):
        os.rmdir(path)