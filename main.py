  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)
  def remove_duplicates(lst):
        return list(set(lst))