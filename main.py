import os
def remove_directory(path):
        os.rmdir(path)
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time