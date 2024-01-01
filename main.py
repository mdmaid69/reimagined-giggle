import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)