def calculate_average(numbers):
        return sum(numbers) / len(numbers)
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)