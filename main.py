  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
  import os
  def get_file_number_of_links(file_name):
        return os.stat(file_name).st_nlink