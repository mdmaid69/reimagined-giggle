  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)
  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]