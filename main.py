import shutil
def delete_directory(path):
        shutil.rmtree(path)
import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)