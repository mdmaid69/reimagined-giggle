import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
import array
def convert_array_to_bytes(array):
        return array.tobytes()