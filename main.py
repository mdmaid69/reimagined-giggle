import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time