import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time