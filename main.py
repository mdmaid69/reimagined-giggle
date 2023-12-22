def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)