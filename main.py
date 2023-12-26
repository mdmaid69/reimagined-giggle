  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()