  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
def is_palindrome(s):
        return s == s[::-1]