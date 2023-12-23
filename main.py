import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)