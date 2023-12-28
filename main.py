  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)