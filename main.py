import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)