  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)