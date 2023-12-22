import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
def calculate_debt_ratio(total_debt, total_assets):
        return total_debt / total_assets