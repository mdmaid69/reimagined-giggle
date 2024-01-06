def is_palindrome(s):
        return s == s[::-1]
  import os
  def get_environment_variable(var_name):
        return os.getenv(var_name)