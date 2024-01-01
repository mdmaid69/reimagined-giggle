def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time
import os
def get_environment_variable(var):
        return os.getenv(var)