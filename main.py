  import os
  def get_file_lspare(file_name):
        return os.stat(file_name).st_lspare
  def remove_duplicates(lst):
        return list(set(lst))