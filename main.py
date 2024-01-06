  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
def is_palindrome(s):
        return s == s[::-1]