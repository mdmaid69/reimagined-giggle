  import os
  def get_file_group(file_name):
        return os.stat(file_name).st_gid
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)