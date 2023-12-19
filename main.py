import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)