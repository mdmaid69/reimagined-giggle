import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
numbers = [1, 2, 3, 4, 5]
print("Sum:", sum(numbers))