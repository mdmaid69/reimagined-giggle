numbers = [1, 2, 3, 4, 5]
print("Average:", sum(numbers) / len(numbers))
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)