import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
import array
def get_array_item_count(array, item):
        return array.count(item)