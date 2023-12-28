import os
def get_file_size(filename):
        return os.path.getsize(filename)
  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]