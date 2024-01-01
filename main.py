  import os
  def set_environment_variable(var_name, value):
        os.environ[var_name] = value
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()