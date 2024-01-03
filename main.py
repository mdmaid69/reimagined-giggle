import glob
def find_files(pattern):
        return glob.glob(pattern)
def calculate_perimeter_rectangle(l, w):
        return 2 * (l + w)