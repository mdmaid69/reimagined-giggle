import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)