import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)