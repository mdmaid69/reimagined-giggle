import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
def calculate_npv(rate, cash_flows):
        return sum(cf / (1 + rate)**i for i, cf in enumerate(cash_flows))