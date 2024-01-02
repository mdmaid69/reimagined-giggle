import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
def remove_duplicates(lst):
        return list(set(lst))