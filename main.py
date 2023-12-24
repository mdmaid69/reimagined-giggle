  import os
  def get_file_inode(file_name):
        return os.stat(file_name).st_ino
def remove_duplicates(lst):
        return list(set(lst))