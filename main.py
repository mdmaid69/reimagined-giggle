import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
import collections
def create_priority_queue():
        return collections.deque()