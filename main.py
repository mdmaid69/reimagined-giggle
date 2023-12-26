import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time