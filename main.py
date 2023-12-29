import re
def split_string(pattern, string):
        return re.split(pattern, string)
import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)