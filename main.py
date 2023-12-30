import os
def get_environment_variable(var):
        return os.getenv(var)
def calculate_simple_interest(principal, rate, time):
        return principal * rate * time