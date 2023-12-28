  import os
  def get_file_size(file_name):
        return os.stat(file_name).st_size
  import os
  def get_base_name(path):
        return os.path.basename(path)