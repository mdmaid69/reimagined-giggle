def is_palindrome(s):
        return s == s[::-1]
  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size