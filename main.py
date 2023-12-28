import re
def split_string(pattern, string):
        return re.split(pattern, string)
import collections
def create_priority_queue():
        return collections.deque()