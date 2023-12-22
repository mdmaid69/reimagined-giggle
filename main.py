def is_palindrome(s):
        return s == s[::-1]
  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)