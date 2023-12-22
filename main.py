  import os
  def delete_file(file_name):
        os.remove(file_name)
  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)