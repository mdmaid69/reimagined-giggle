def is_palindrome(s):
        return s == s[::-1]
  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)