import collections
def create_user_string():
        return collections.UserString()
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)