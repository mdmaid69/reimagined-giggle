def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal
import os
def get_file_size(filename):
        return os.path.getsize(filename)