import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))