import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)