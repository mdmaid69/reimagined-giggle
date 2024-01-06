  import os
  def get_file_number_of_links(file_name):
        return os.stat(file_name).st_nlink
  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)