  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()