def calculate_average(lst):
        return sum(lst) / len(lst)
  def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)