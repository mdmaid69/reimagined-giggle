import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
def calculate_simple_interest(principal, rate, time):
        return principal * rate * time