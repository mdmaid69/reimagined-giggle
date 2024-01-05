  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)