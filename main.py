import glob
def find_files(pattern):
        return glob.glob(pattern)
def calculate_pressure(force, area):
        return force / area