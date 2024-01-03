import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)
def calculate_average(numbers):
        return sum(numbers) / len(numbers)