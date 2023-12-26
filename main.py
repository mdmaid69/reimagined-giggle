import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])