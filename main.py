  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()