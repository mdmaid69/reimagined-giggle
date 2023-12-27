import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()