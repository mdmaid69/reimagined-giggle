  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()