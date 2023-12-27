def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)