def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)