  import os
  def get_file_uid(file_name):
        return os.stat(file_name).st_uid
def is_even(n):
        return n % 2 == 0