  def calculate_perimeter_rectangle(l, w):
        return 2 * (l + w)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()