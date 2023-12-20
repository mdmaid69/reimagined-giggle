import os
def get_environment_variable(var):
        return os.getenv(var)
import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)