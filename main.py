  def square_number(x):
        return x**2
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()