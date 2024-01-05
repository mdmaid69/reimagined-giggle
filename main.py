import os
def get_current_working_directory():
        return os.getcwd()
n = 10
print("Powers of 2:", [2**x for x in range(n)])