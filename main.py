def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time
import collections
def create_default_dict(default_type):
        return collections.defaultdict(default_type)