  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"
import os
def list_files_in_directory(path):
        return os.listdir(path)