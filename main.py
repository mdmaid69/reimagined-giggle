  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"
def is_palindrome(s):
        return s == s[::-1]