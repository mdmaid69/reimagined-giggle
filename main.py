  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
  import os
  def get_base_name(path):
        return os.path.basename(path)