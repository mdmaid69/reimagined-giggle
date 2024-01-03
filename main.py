import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"