import glob
def find_files(pattern):
        return glob.glob(pattern)
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time