  import os
  def get_file_uid(file_name):
        return os.stat(file_name).st_uid
  import os
  def split_path(path):
        return os.path.split(path)