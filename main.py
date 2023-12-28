import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time