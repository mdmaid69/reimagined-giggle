import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()