  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)