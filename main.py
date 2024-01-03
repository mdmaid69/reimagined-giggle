import glob
def find_files(pattern):
        return glob.glob(pattern)
def calculate_power(work, time):
        return work / time