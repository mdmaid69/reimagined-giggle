import array
def iterate_over_array(array):
        for item in array:
        print(item)
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)