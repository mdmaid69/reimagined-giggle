import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)