import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)