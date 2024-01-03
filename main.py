def calculate_roi(gain, cost):
        return (gain - cost) / cost
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)