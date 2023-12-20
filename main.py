def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)