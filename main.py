import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import shutil
def move_file(src, dst):
        shutil.move(src, dst)