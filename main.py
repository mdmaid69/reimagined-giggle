  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()