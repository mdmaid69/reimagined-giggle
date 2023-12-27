import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)