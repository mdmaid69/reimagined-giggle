import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)