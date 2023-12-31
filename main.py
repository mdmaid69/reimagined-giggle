import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()
  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"