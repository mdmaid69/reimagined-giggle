import os
def get_file_size(filename):
        return os.path.getsize(filename)
n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])