import os
def change_working_directory(path):
        os.chdir(path)
def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal