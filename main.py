import os
def get_file_modification_time(filename):
        return os.path.getmtime(filename)
  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)