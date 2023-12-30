import os
def change_working_directory(path):
        os.chdir(path)
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]