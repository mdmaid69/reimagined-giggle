import os
def get_environment_variable(var):
        return os.getenv(var)
import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)