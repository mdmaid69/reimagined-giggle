def calculate_quick_ratio(current_assets, inventory, current_liabilities):
        return (current_assets - inventory) / current_liabilities
import collections
def create_named_tuple(name, fields):
        return collections.namedtuple(name, fields)