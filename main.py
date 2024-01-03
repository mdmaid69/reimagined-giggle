  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
import re
print(re.match("h.*o", "hello world"))