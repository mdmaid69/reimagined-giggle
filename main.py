  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)
import hashlib
def hash_string(s):
        return hashlib.sha256(s.encode()).hexdigest()