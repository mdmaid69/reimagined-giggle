  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
import os
def get_file_size(filename):
        return os.path.getsize(filename)