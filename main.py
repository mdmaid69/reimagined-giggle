import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
  def remove_duplicates(lst):
        return list(set(lst))