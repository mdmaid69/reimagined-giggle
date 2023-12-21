  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"
  def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)