import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
import re
def split_string(pattern, string):
        return re.split(pattern, string)