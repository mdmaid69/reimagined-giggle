def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)