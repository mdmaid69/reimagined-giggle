  import os
  def get_file_birthtime(file_name):
        return os.stat(file_name).st_birthtime
  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size