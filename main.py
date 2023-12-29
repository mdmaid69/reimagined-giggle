def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time
import os
def get_file_size(filename):
        return os.path.getsize(filename)