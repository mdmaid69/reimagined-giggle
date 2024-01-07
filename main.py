  import os
  def delete_file(file_name):
        os.remove(file_name)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()