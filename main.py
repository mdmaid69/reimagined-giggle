import os
def get_environment_variable(var):
        return os.getenv(var)
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time