import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import re
def split_string(pattern, string):
        return re.split(pattern, string)