  import os
  def get_base_name(path):
        return os.path.basename(path)
  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]