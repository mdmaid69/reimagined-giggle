import os
def remove_directory(path):
        os.rmdir(path)
  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]