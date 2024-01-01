import glob
def find_files(pattern):
        return glob.glob(pattern)
def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time