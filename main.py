def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time
import os
def list_files_in_directory(path):
        return os.listdir(path)