import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)