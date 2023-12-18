import glob
def find_files(pattern):
        return glob.glob(pattern)
def calculate_roi(gain, cost):
        return (gain - cost) / cost