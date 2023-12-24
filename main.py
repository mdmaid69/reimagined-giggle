import os
def get_file_size(filename):
        return os.path.getsize(filename)
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time