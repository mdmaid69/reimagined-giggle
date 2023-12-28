  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
  import os
  def delete_file(file_name):
        os.remove(file_name)