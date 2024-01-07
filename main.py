import shutil
def move_file(src, dst):
        shutil.move(src, dst)
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)