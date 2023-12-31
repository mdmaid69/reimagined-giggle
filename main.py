  import os
  def delete_file(file_name):
        os.remove(file_name)
  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)