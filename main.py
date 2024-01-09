def find_common_elements(list1, list2):
        return set(list1) & set(list2)
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)