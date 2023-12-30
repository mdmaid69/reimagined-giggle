  import os
  def delete_file(file_name):
        os.remove(file_name)
  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"