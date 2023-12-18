import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)
import collections
def create_stack():
        return collections.deque()