def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)