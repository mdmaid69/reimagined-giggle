import shutil
def delete_directory(path):
        shutil.rmtree(path)
import re
def split_string(pattern, string):
        return re.split(pattern, string)