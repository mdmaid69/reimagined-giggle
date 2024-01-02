import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time