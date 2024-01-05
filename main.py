def find_union(list1, list2):
        return set(list1) | set(list2)
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)