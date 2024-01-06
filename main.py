import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
def calculate_average(lst):
        return sum(lst) / len(lst)