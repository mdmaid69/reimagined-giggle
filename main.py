import tempfile
def create_temp_file():
        return tempfile.NamedTemporaryFile(delete=False)
  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)