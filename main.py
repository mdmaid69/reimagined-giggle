import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import shutil
def delete_directory(path):
        shutil.rmtree(path)