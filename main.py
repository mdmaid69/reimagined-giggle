  import os
  def get_file_number_of_links(file_name):
        return os.stat(file_name).st_nlink
  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size