  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()