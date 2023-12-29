import re
def split_string(pattern, string):
        return re.split(pattern, string)
import shutil
def move_file(src, dst):
        shutil.move(src, dst)