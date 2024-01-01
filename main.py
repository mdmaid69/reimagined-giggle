import os
def get_file_size(filename):
        return os.path.getsize(filename)
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))