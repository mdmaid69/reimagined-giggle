def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal
import os
def list_files_in_directory(path):
        return os.listdir(path)