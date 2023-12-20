import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
  def cube_number(x):
        return x**3