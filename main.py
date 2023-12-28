import shutil
def delete_directory(path):
        shutil.rmtree(path)
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)