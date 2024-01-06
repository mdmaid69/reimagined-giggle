  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size
  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags