  import os
  def get_file_birthtime_ns(file_name):
        return os.stat(file_name).st_birthtime_ns
import tempfile
def create_temp_directory():
        return tempfile.TemporaryDirectory()