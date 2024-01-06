import os
def get_environment_variable(var):
        return os.getenv(var)
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)