import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)