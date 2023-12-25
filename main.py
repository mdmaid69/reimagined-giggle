import os
def get_current_working_directory():
        return os.getcwd()
n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])