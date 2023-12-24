import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
def calculate_profit_margin(revenue, cost):
        return (revenue - cost) / revenue