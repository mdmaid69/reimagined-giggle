import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
def calculate_eps(net_income, shares_outstanding):
        return net_income / shares_outstanding