  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)
  def remove_duplicates(lst):
        return list(set(lst))