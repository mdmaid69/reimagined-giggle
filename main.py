import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))