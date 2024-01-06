import os
def list_files_in_directory(path):
        return os.listdir(path)
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)