  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
import re
def find_pattern(pattern, string):
        return re.findall(pattern, string)