import os
def get_current_working_directory():
        return os.getcwd()
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)