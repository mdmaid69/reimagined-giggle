import re
def split_string(pattern, string):
        return re.split(pattern, string)
import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)