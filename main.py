import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))