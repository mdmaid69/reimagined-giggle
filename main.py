list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Common elements:", set(list1) & set(list2))
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)