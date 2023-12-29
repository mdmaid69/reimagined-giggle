import shutil
def delete_directory(path):
        shutil.rmtree(path)
def calculate_average(numbers):
        return sum(numbers) / len(numbers)