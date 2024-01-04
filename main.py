import os
def get_file_size(filename):
        return os.path.getsize(filename)
  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)