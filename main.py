import glob
def find_files(pattern):
        return glob.glob(pattern)
def calculate_simple_interest(principal, rate, time):
        return principal * rate * time