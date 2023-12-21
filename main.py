  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
  def count_elements(lst):
        return len(lst)