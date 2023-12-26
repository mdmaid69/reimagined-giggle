import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)