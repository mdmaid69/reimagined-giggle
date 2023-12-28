import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)