  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
  def remove_duplicates(lst):
        return list(set(lst))