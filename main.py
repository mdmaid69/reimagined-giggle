  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]