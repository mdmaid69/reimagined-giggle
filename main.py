  import os
  def get_file_mtime(file_name):
        return os.stat(file_name).st_mtime
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()