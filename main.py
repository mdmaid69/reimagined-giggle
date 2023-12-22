def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)
import os
def list_files_in_directory(path):
        return os.listdir(path)