import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
  def convert_to_octal(n):
        return oct(n)