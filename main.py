import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)