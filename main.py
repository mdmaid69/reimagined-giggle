import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)