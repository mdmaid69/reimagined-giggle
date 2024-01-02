  import os
  def get_file_number_of_links(file_name):
        return os.stat(file_name).st_nlink
  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)