import glob
def find_files(pattern):
        return glob.glob(pattern)
def calculate_average(numbers):
        return sum(numbers) / len(numbers)