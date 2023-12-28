import array
def create_array(typecode, initializer):
        return array.array(typecode, initializer)
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)