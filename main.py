import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)