  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
def remove_duplicates(lst):
        return list(set(lst))