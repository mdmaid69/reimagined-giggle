  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()