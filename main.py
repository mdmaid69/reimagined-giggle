import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)