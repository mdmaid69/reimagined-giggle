  import os
  def get_file_lspare(file_name):
        return os.stat(file_name).st_lspare
  import os
  def get_file_size(file_name):
        return os.stat(file_name).st_size