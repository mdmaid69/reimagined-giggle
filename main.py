  import os
  def get_current_directory():
        return os.getcwd()
  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime