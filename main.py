import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)