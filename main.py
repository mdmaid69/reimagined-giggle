  def convert_to_hex(n):
        return hex(n)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()