  import os
  def get_file_qspare(file_name):
        return os.stat(file_name).st_qspare
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()