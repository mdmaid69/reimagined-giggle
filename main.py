def is_even(n):
        return n % 2 == 0
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)