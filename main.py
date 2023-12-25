numbers = [1, 2, 3, 4, 5]
print("Average:", sum(numbers) / len(numbers))
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)