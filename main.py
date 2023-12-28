import shutil
def move_file(src, dst):
        shutil.move(src, dst)
import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)