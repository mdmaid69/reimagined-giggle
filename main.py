  import os
  def get_file_mtime(file_name):
        return os.stat(file_name).st_mtime
import shutil
def delete_directory(path):
        shutil.rmtree(path)