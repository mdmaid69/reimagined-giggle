def calculate_average(numbers):
        return sum(numbers) / len(numbers)
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()