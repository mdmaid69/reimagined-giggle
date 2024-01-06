import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)
  import os
  def split_path(path):
        return os.path.split(path)