  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
import os
def get_file_size(filename):
        return os.path.getsize(filename)