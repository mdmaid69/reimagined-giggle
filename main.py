def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)