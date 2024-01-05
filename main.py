def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time
import os
def change_working_directory(path):
        os.chdir(path)