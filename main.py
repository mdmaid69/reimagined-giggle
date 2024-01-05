import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
def calculate_return_on_equity(net_income, total_equity):
        return net_income / total_equity