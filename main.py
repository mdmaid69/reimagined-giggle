import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
def sort_numbers(numbers):
        return sorted(numbers)