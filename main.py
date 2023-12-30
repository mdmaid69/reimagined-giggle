import os
def get_environment_variable(var):
        return os.getenv(var)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)