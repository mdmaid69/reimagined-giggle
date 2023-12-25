import shutil
def delete_directory(path):
        shutil.rmtree(path)
def calculate_average(lst):
        return sum(lst) / len(lst)