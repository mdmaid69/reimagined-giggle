import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)
import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)