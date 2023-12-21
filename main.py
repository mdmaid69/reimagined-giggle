import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)