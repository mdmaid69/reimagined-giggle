  import os
  def get_directory_name(path):
        return os.path.dirname(path)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()