  import os
  def get_file_number_of_links(file_name):
        return os.stat(file_name).st_nlink
import os
def get_file_creation_time(filename):
        return os.path.getctime(filename)