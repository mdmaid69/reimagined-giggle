import re
def replace_all_occurrences(pattern, replacement, string):
        return re.sub(pattern, replacement, string)
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value