  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()