import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
  import os
  def delete_file(file_name):
        os.remove(file_name)