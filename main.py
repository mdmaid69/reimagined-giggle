import collections
def create_ordered_dict():
        return collections.OrderedDict()
def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))