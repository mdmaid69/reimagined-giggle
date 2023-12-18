  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime
  import os
  def get_base_name(path):
        return os.path.basename(path)