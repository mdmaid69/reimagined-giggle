  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()