import glob
def find_files(pattern):
        return glob.glob(pattern)
def calculate_average(lst):
        return sum(lst) / len(lst)