  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime
  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen