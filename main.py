import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
numbers = [1, 2, 3, 4, 5]
print("Average:", sum(numbers) / len(numbers))