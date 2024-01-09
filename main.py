  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)
import os
def get_file_size(filename):
        return os.path.getsize(filename)