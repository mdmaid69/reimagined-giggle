  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)
  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value