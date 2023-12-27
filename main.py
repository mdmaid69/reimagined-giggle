  import os
  def delete_file(file_name):
        os.remove(file_name)
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)