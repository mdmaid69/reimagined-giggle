import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal