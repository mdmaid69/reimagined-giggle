import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
import shutil
def delete_directory(path):
        shutil.rmtree(path)