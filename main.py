  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()