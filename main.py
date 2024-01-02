  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]