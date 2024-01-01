import glob
def find_files(pattern):
        return glob.glob(pattern)
def calculate_perpetuity(payment, rate):
        return payment / rate