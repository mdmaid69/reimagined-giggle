import re
def replace_pattern(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import collections
def create_priority_queue():
        return collections.deque()