import os
def get_file_size(filename):
        return os.path.getsize(filename)
def calculate_simple_interest(principal, rate, time):
        return principal * rate * time