  import os
  def get_directory_name(path):
        return os.path.dirname(path)
def is_palindrome(s):
        return s == s[::-1]