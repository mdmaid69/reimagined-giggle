def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
import os
def remove_directory(path):
        os.rmdir(path)