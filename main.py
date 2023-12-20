  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
  import os
  def delete_file(file_name):
        os.remove(file_name)