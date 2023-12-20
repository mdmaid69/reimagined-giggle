def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)