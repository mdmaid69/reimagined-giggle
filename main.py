def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
import os
def get_current_working_directory():
        return os.getcwd()