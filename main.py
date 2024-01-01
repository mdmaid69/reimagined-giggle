def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)