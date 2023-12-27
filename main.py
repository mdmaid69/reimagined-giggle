import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)