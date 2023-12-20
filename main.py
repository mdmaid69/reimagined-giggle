  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]