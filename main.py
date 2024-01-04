import os
def list_files_in_directory(path):
        return os.listdir(path)
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time