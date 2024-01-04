import os
def get_file_size(filename):
        return os.path.getsize(filename)
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)