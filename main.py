  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino
def is_palindrome(s):
        return s == s[::-1]