  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)
  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]