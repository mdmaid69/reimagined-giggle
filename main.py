import collections
def create_stack():
        return collections.deque()
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)