import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)
def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))