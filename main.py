import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink