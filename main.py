  import os
  def get_file_ctime_ns(file_name):
        return os.stat(file_name).st_ctime_ns
  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size