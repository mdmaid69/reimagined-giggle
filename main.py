import os
def change_working_directory(path):
        os.chdir(path)
import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)