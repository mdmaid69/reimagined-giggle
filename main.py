import os
def list_files_in_directory(path):
        return os.listdir(path)
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time