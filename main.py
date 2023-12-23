import glob
def find_files(pattern):
        return glob.glob(pattern)
def calculate_annuity(payment, rate, time):
        return payment * ((1 - (1 + rate)**-time) / rate)