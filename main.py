  import os
  def get_file_blocks(file_name):
        return os.stat(file_name).st_blocks
  import os
  def get_file_number_of_links(file_name):
        return os.stat(file_name).st_nlink