def is_palindrome(s):
        return s == s[::-1]
  import re
  def replace_all_occurrences(pattern, replace_with, string):
        return re.sub(pattern, replace_with, string)