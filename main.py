def is_palindrome(s):
        return s == s[::-1]
  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"