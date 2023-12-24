  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]
import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)