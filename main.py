  import os
  def get_base_name(path):
        return os.path.basename(path)
def is_palindrome(s):
        return s == s[::-1]