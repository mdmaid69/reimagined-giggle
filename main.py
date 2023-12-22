def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)