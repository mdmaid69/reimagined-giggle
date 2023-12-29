  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size
  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)