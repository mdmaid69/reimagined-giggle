  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size
import shutil
def delete_directory(path):
        shutil.rmtree(path)