  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
import os
def remove_directory(path):
        os.rmdir(path)