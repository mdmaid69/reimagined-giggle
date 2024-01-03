import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
import array
def get_array_as_format(array, format_spec):
        return format(array, format_spec)