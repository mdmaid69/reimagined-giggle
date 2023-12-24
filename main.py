import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
import os
def get_environment_variable(var):
        return os.getenv(var)