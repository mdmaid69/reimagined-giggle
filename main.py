def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
  def remove_duplicates(lst):
        return list(set(lst))