import os
def get_environment_variable(var):
        return os.getenv(var)
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)