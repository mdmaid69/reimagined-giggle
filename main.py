import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"