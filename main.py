  import os
  def get_file_number_of_links(file_name):
        return os.stat(file_name).st_nlink
  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)