  import os
  def get_directory_name(path):
        return os.path.dirname(path)
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]