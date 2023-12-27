  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]
def remove_duplicates(lst):
        return list(set(lst))