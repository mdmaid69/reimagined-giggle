import shutil
def move_file(src, dst):
        shutil.move(src, dst)
import re
def split_string(pattern, string):
        return re.split(pattern, string)