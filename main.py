import collections
def create_user_string():
        return collections.UserString()
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)