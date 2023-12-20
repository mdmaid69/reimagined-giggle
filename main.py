  import os
  def get_file_ctime_ns(file_name):
        return os.stat(file_name).st_ctime_ns
def convert_to_hex(n):
        return hex(n)