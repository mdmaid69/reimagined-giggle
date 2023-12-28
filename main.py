import os
def change_working_directory(path):
        os.chdir(path)
import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)