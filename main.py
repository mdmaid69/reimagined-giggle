import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
  import os
  def get_file_ctime_ns(file_name):
        return os.stat(file_name).st_ctime_ns