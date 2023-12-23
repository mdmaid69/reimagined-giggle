  import os
  def get_file_blksize(file_name):
        return os.stat(file_name).st_blksize
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()