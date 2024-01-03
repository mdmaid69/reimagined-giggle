import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
def calculate_return_on_assets(net_income, total_assets):
        return net_income / total_assets