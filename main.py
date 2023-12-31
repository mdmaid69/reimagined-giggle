import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
  def remove_duplicates(lst):
        return list(set(lst))