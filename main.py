  import os
  def get_file_dev(file_name):
        return os.stat(file_name).st_dev
  import os
  def get_base_name(path):
        return os.path.basename(path)