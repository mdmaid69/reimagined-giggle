def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
import glob
def find_files(pattern):
        return glob.glob(pattern)