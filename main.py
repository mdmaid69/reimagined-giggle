import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)
import collections
def create_priority_queue():
        return collections.deque()