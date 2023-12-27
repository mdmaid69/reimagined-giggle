import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)