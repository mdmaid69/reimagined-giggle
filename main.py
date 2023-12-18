  def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"