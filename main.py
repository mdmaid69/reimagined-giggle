  import os
  def get_file_ctime_ns(file_name):
        return os.stat(file_name).st_ctime_ns
def is_odd(n):
        return n % 2 != 0