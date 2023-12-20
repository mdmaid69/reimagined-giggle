  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)
def is_palindrome(s):
        return s == s[::-1]