  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()