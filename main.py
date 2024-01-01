import os
def change_working_directory(path):
        os.chdir(path)
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)