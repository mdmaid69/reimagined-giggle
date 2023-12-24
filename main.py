  def calculate_average(lst):
        return sum(lst) / len(lst) if len(lst) != 0 else "List is empty"
def calculate_factorial(n):
        return 1 if n == 0 else n * calculate_factorial(n-1)