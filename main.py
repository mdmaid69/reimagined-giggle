import os
def get_current_working_directory():
        return os.getcwd()
numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])