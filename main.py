  import os
  def get_file_ctime(file_name):
        return os.stat(file_name).st_ctime
import shutil
def delete_directory(path):
        shutil.rmtree(path)