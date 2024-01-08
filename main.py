def reverse_string(s):
        return s[::-1]
  import os
  def get_file_ctime_ns(file_name):
        return os.stat(file_name).st_ctime_ns