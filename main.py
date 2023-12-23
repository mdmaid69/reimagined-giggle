  import os
  def get_file_owner(file_name):
        return os.stat(file_name).st_uid
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()