def is_palindrome(s):
        return s == s[::-1]
  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]