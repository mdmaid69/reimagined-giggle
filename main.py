  import os
  def get_base_name(path):
        return os.path.basename(path)
  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)