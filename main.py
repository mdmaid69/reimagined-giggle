  import os
  def get_file_owner(file_name):
        return os.stat(file_name).st_uid
def remove_duplicates(lst):
        return list(set(lst))