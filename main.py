import array
def convert_string_to_array(string, typecode):
        a = array.array(typecode)
        a.fromstring(string)
        return a
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)