import glob
def find_files(pattern):
        return glob.glob(pattern)
def calculate_force(mass, acceleration):
        return mass * acceleration