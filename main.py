  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)