import array
def convert_list_to_array(list, typecode):
        return array.array(typecode, list)
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)