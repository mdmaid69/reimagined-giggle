  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size