  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]
  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"