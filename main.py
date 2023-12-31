  import os
  def get_file_dev(file_name):
        return os.stat(file_name).st_dev
  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)