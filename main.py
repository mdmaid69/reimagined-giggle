  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)
  import os
  def get_file_mtime(file_name):
        return os.stat(file_name).st_mtime