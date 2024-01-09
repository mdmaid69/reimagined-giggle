import glob
def find_files(pattern):
        return glob.glob(pattern)
def calculate_work(force, distance):
        return force * distance