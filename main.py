import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])