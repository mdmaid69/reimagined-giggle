  import os
  def get_file_lspare(file_name):
        return os.stat(file_name).st_lspare
  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)