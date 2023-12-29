  import os
  def split_path(path):
        return os.path.split(path)
def is_palindrome(s):
        return s == s[::-1]