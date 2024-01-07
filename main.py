import os
def change_working_directory(path):
        os.chdir(path)
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time