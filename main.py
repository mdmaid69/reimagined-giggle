import re
def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
import collections
def create_counter():
        return collections.Counter()