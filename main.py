import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"