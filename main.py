import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
def convert_to_binary(n):
        return bin(n)