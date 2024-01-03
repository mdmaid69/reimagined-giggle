def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)