def convert_to_hex(n):
        return hex(n)
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)