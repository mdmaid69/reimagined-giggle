  import os
  def get_file_number_of_links(file_name):
        return os.stat(file_name).st_nlink
  import os
  def split_path(path):
        return os.path.split(path)