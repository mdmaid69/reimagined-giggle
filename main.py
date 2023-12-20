import glob
def find_files(pattern):
        return glob.glob(pattern)
def calculate_speed(distance, time):
        return distance / time