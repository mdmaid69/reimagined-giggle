import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
def reverse_string(s):
        return s[::-1]