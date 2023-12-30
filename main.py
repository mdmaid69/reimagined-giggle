import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
def calculate_current_ratio(current_assets, current_liabilities):
        return current_assets / current_liabilities