  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()