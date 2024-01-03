  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]
  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)