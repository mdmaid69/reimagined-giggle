import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import os
def get_environment_variable(var):
        return os.getenv(var)