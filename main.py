import os
def get_current_working_directory():
        return os.getcwd()
numbers = [1, 2, 3, 4, 5]
print("Squared:", [n**2 for n in numbers])