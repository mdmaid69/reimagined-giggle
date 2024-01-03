import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)