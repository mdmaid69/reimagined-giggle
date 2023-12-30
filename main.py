import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
def calculate_perpetuity(payment, rate):
        return payment / rate