import os
def get_file_size(filename):
        return os.path.getsize(filename)
def calculate_average(numbers):
        return sum(numbers) / len(numbers)