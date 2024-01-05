import array
def convert_unicode_to_array(unicode, typecode):
        a = array.array(typecode)
        a.fromunicode(unicode)
        return a
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)