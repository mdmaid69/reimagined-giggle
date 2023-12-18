  def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"