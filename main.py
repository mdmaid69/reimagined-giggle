  import os
  def get_file_group(file_name):
        return os.stat(file_name).st_gid
  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)