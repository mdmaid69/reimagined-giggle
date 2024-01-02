import collections
def create_user_list():
        return collections.UserList()
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)