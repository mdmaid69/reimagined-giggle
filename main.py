def calculate_profit_margin(revenue, cost):
        return (revenue - cost) / revenue
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)