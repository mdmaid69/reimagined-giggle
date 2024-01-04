  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"
  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)