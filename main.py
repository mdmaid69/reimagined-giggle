  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()