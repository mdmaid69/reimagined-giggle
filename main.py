  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
import re
def split_by_pattern(pattern, string):
        return re.split(pattern, string)