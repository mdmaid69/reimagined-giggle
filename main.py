import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)