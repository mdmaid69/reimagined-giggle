  import os
  def delete_file(file_name):
        os.remove(file_name)
import os
def get_environment_variable(var):
        return os.getenv(var)