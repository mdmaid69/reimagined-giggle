  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size
  import os
  def get_file_qspare(file_name):
        return os.stat(file_name).st_qspare