  import os
  def get_file_group(file_name):
        return os.stat(file_name).st_gid
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()