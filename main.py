import collections
def create_user_string():
        return collections.UserString()
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)