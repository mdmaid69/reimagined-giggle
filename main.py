def calculate_average(lst):
        return sum(lst) / len(lst)
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()