import collections
def create_user_dict():
        return collections.UserDict()
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)