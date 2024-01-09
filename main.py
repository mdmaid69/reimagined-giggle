  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)