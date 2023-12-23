def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal
import glob
def find_files(pattern):
        return glob.glob(pattern)