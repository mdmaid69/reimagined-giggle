import glob
def find_files(pattern):
        return glob.glob(pattern)
def calculate_area(radius):
        return 3.14 * radius * radius