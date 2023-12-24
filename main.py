  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino
  import os
  def split_path(path):
        return os.path.split(path)