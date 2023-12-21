import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)