  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()