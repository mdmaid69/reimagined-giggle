  import os
  def get_file_lspare(file_name):
        return os.stat(file_name).st_lspare
  import os
  def split_path(path):
        return os.path.split(path)