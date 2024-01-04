import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import collections
def create_ordered_dict():
        return collections.OrderedDict()