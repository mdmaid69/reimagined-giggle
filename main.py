import glob
def find_files(pattern):
        return glob.glob(pattern)
def calculate_acceleration(speed, time):
        return speed / time