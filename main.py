  import os
  def delete_file(file_name):
        os.remove(file_name)
import os
def get_file_size(filename):
        return os.path.getsize(filename)