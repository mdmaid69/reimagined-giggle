  import os
  def get_file_dev(file_name):
        return os.stat(file_name).st_dev
  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size