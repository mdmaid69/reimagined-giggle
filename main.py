  import os
  def get_file_blocks(file_name):
        return os.stat(file_name).st_blocks
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()