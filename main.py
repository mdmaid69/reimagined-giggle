  import re
  def find_all_occurrences(pattern, string):
        return re.findall(pattern, string)
def is_palindrome(s):
        return s == s[::-1]