import os
def get_current_working_directory():
        return os.getcwd()
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)