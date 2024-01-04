def calculate_average(lst):
        return sum(lst) / len(lst)
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)