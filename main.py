import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
import array
def get_array_as_format(array, format_spec):
        return format(array, format_spec)