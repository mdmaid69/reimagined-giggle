import collections
def create_user_dict():
        return collections.UserDict()
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)