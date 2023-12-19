  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino
def count_elements(lst):
        return len(lst)