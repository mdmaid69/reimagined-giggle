def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)