  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)