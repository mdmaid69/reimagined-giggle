  import os
  def get_file_ctime(file_name):
        return os.stat(file_name).st_ctime
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()