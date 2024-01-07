  import os
  def split_path(path):
        return os.path.split(path)
  import os
  def get_file_blksize(file_name):
        return os.stat(file_name).st_blksize