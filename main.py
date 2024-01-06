  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
def remove_duplicates(lst):
        return list(set(lst))