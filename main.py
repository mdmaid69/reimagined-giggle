  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)
def is_even(n):
        return n % 2 == 0