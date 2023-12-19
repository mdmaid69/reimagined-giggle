import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)