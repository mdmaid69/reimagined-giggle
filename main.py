  import os
  def get_file_number_of_links(file_name):
        return os.stat(file_name).st_nlink
  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"