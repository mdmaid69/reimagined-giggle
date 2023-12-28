import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
  import os
  def split_path(path):
        return os.path.split(path)