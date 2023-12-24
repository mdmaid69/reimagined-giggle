import os
def remove_directory(path):
        os.rmdir(path)
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time