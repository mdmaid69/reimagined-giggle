import collections
def count_elements(iterable):
        return collections.Counter(iterable)
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)