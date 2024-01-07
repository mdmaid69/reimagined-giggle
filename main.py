import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)