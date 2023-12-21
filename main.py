def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
import collections
def create_ordered_dict():
        return collections.OrderedDict()