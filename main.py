n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])
  def find_min(lst):
        return min(lst) if len(lst) != 0 else "List is empty"