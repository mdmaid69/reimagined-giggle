import os
def get_file_size(filename):
        return os.path.getsize(filename)
numbers = [1, 2, 3, 4, 5]
print("Average:", sum(numbers) / len(numbers))