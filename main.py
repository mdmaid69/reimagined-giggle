import glob
def find_files(pattern):
        return glob.glob(pattern)
def calculate_area_triangle(b, h):
        return 0.5 * b * h