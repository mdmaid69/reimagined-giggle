  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size
  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)