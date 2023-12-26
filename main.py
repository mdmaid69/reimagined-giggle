def is_palindrome(s):
        return s == s[::-1]
  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)