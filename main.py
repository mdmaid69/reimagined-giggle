import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()
  import os
  def get_file_mtime_ns(file_name):
        return os.stat(file_name).st_mtime_ns