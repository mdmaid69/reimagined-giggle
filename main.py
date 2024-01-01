import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
import os
def change_working_directory(path):
        os.chdir(path)