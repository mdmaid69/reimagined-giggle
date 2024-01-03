import os
def change_working_directory(path):
        os.chdir(path)
def calculate_simple_interest(principal, rate, time):
        return principal * rate * time