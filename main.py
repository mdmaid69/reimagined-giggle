import os
def change_working_directory(path):
        os.chdir(path)
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)