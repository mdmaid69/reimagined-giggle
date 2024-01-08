  import os
  def delete_file(file_name):
        os.remove(file_name)
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)