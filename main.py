import glob
def find_files(pattern):
        return glob.glob(pattern)
def calculate_area_circle(r):
        return 3.14 * r**2