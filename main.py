  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)
  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)