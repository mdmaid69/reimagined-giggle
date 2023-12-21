  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)
  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime