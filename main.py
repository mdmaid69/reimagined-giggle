import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()