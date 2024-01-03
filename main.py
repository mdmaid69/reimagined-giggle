import glob
def find_files(pattern):
        return glob.glob(pattern)
def calculate_density(mass, volume):
        return mass / volume