import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)
import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)