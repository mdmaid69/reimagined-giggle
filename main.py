  import os
  def get_current_directory():
        return os.getcwd()
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()