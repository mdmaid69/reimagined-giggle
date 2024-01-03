  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
def is_palindrome(s):
        return s == s[::-1]