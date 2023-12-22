  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()