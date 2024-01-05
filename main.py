  import os
  def get_current_directory():
        return os.getcwd()
import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)