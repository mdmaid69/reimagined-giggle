  import os
  def get_current_directory():
        return os.getcwd()
  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size