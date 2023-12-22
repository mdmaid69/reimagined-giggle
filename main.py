import re
def split_string(pattern, string):
        return re.split(pattern, string)
import os
def change_working_directory(path):
        os.chdir(path)