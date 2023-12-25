  import os
  def delete_file(file_name):
        os.remove(file_name)
  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"