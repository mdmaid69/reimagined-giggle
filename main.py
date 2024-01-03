  import os
  def get_base_name(path):
        return os.path.basename(path)
import os
def change_working_directory(path):
        os.chdir(path)