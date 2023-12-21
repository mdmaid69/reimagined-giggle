import os
def get_current_working_directory():
        return os.getcwd()
import re
def split_string(pattern, string):
        return re.split(pattern, string)