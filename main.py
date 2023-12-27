def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time
import os
def remove_directory(path):
        os.rmdir(path)