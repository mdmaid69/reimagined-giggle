  import os
  def get_file_uid(file_name):
        return os.stat(file_name).st_uid
import shutil
def delete_directory(path):
        shutil.rmtree(path)