  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()