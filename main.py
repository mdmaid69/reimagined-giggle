  import os
  def get_file_mtime_ns(file_name):
        return os.stat(file_name).st_mtime_ns
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)