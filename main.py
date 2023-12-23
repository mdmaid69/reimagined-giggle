import array
def get_array_from_list(list, typecode):
        return array.array(typecode, list)
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)