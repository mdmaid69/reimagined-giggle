  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)