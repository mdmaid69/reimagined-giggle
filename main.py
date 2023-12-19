  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]