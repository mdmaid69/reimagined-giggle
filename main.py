  import os
  def get_base_name(path):
        return os.path.basename(path)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()