import collections
def create_queue():
        return collections.deque()
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)