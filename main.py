  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()