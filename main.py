  import os
  def get_file_blocks(file_name):
        return os.stat(file_name).st_blocks
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)