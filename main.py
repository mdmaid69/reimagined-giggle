  import os
  def get_base_name(path):
        return os.path.basename(path)
  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino