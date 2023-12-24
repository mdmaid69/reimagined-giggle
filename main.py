  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()