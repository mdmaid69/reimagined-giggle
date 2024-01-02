  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()