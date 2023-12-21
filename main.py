import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)