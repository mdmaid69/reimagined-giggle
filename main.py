  import os
  def get_file_gid(file_name):
        return os.stat(file_name).st_gid
  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)