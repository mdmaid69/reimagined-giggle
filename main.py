import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
  import sys
  def get_python_version():
        return sys.version