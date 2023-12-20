  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
def remove_duplicates(lst):
        return list(set(lst))