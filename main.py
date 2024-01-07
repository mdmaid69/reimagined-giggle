  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size
  import os
  def get_file_group(file_name):
        return os.stat(file_name).st_gid