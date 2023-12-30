  import os
  def delete_file(file_name):
        os.remove(file_name)
  def remove_duplicates(lst):
        return list(set(lst))