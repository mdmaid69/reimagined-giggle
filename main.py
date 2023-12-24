  def find_max(lst):
        return max(lst) if len(lst) != 0 else "List is empty"
  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)