  import os
  def get_file_birthtime_ns(file_name):
        return os.stat(file_name).st_birthtime_ns
import shutil
def delete_directory(path):
        shutil.rmtree(path)