  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()