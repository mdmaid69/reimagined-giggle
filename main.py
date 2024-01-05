  import os
  def get_file_number_of_links(file_name):
        return os.stat(file_name).st_nlink
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value