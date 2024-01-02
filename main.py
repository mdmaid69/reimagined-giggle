import glob
def find_files(pattern):
        return glob.glob(pattern)
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time