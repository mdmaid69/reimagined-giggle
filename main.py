import glob
def find_files(pattern):
        return glob.glob(pattern)
def calculate_volume(length, width, height):
        return length * width * height