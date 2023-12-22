  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]
  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)