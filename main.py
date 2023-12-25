import collections
def create_queue():
        return collections.deque()
def calculate_pe_ratio(price_per_share, eps):
        return price_per_share / eps