  import os
  def get_directory_name(path):
        return os.path.dirname(path)
  import os
  def get_file_permissions(file_name):
        return os.stat(file_name).st_mode