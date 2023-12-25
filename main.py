import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
def calculate_simple_interest(principal, rate, time):
        return principal * rate * time