  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
  import os
  def get_base_name(path):
        return os.path.basename(path)