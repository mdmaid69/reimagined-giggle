  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()