import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)