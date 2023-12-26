  import os
  def delete_file(file_name):
        os.remove(file_name)
import os
def list_files_in_directory(path):
        return os.listdir(path)