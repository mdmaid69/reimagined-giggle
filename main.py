def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)