def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)
import glob
def find_files(pattern):
        return glob.glob(pattern)