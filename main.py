import os
def get_environment_variable(var):
        return os.getenv(var)
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)