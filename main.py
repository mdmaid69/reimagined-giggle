import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)
import re
def split_string(pattern, string):
        return re.split(pattern, string)