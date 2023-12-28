  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)